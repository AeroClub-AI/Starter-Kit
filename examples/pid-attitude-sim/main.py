import numpy as np
import matplotlib.pyplot as plt
import yaml
import os
import csv

def load_config(path="config.yaml"):
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def pid_step(error, integral, prev_error, dt, Kp, Ki, Kd, u_max):
    integral += error * dt
    derivative = (error - prev_error) / dt if dt > 0 else 0.0
    u = Kp * error + Ki * integral + Kd * derivative
    # Actuator saturation & simple anti-windup
    u_sat = np.clip(u, -u_max, u_max)
    if abs(u) > u_max:
        integral -= error * dt  # freeze integral when saturated
    return u_sat, integral, u_sat

def simulate(cfg):
    I = cfg['physics']['inertia']
    c = cfg['physics']['damping']
    u_max = cfg['physics']['max_torque']
    Kp, Ki, Kd = cfg['pid']['Kp'], cfg['pid']['Ki'], cfg['pid']['Kd']
    T = cfg['simulation']['duration']
    dt = cfg['simulation']['dt']
    steps = int(T / dt)

    time = np.linspace(0, T, steps)
    theta = np.zeros(steps)
    omega = np.zeros(steps)
    u_ctrl = np.zeros(steps)
    setpoint = cfg['simulation']['setpoint']

    theta[0] = cfg['simulation']['initial_angle']
    omega[0] = cfg['simulation']['initial_rate']

    integral = 0.0
    prev_error = setpoint - theta[0]

    for i in range(1, steps):
        error = setpoint - theta[i-1]
        u, integral, _ = pid_step(error, integral, prev_error, dt, Kp, Ki, Kd, u_max)
        u_ctrl[i] = u

        # Dynamics: I*alpha + c*omega = u  =>  alpha = (u - c*omega) / I
        alpha = (u - c * omega[i-1]) / I

        # Euler integration
        omega[i] = omega[i-1] + alpha * dt
        theta[i] = theta[i-1] + omega[i] * dt

        prev_error = error

    return time, theta, omega, u_ctrl, setpoint

def plot_and_save(time, theta, omega, u_ctrl, setpoint, cfg):
    os.makedirs(cfg['output']['dir'], exist_ok=True)

    # Save CSV
    data_path = os.path.join(cfg['output']['dir'], cfg['output']['data_file'])
    with open(data_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['time_s', 'angle_rad', 'rate_rad_s', 'control_Nm'])
        for t, th, om, uc in zip(time, theta, omega, u_ctrl):
            writer.writerow([t, th, om, uc])

    # Plot
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 7), sharex=True)
    ax1.plot(time, theta, 'b-', linewidth=2, label='Actual Angle')
    ax1.axhline(setpoint, color='r', linestyle='--', label='Setpoint')
    ax1.set_ylabel('Angle (rad)')
    ax1.legend()
    ax1.grid(True)

    ax2.plot(time, u_ctrl, 'g-', linewidth=2, label='Control Torque')
    ax2.set_xlabel('Time (s)')
    ax2.set_ylabel('Torque (N*m)')
    ax2.legend()
    ax2.grid(True)

    plt.tight_layout()
    plot_path = os.path.join(cfg['output']['dir'], cfg['output']['plot_file'])
    plt.savefig(plot_path, dpi=150)
    print(f"✅ Results saved to {cfg['output']['dir']}")

if __name__ == "__main__":
    print("🎯 Starting PID Attitude Control Simulation...")
    cfg = load_config()
    time, theta, omega, u_ctrl, setpoint = simulate(cfg)
    plot_and_save(time, theta, omega, u_ctrl, setpoint, cfg)
    print("🎉 Done. Check output/ for data & plots.")