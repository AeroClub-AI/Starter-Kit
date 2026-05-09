import numpy as np
import matplotlib.pyplot as plt
import yaml
import os
import csv

def load_config(path="config.yaml"):
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def solve_kepler(M, e, tol=1e-8, max_iter=50):
    """Solve Kepler's equation: E - e*sin(E) = M using Newton-Raphson"""
    E = M.copy()
    for _ in range(max_iter):
        dE = (E - e * np.sin(E) - M) / (1 - e * np.cos(E))
        E -= dE
        if np.all(np.abs(dE) < tol):
            break
    return E

def propagate_orbit(cfg):
    # Extract parameters
    a = cfg['orbit']['semi_major_axis']
    e = cfg['orbit']['eccentricity']
    i = np.radians(cfg['orbit']['inclination'])
    Omega = np.radians(cfg['orbit']['raan'])
    omega = np.radians(cfg['orbit']['arg_perigee'])
    M0 = np.radians(cfg['orbit']['mean_anomaly'])
    mu = cfg['constants']['mu_earth']
    duration = cfg['simulation']['duration']
    dt = cfg['simulation']['step']

    n = np.sqrt(mu / a**3)  # Mean motion (rad/s)
    t = np.arange(0, duration + dt, dt)
    M = (M0 + n * t) % (2 * np.pi)

    E = solve_kepler(M, e)

    # True anomaly & radius
    nu = 2 * np.arctan2(np.sqrt(1+e) * np.sin(E/2), np.sqrt(1-e) * np.cos(E/2))
    r = a * (1 - e * np.cos(E))

    # Perifocal coordinates
    xp = r * np.cos(nu)
    yp = r * np.sin(nu)

    # Rotation matrix: Perifocal -> ECI
    ci, si = np.cos(i), np.sin(i)
    co, so = np.cos(Omega), np.sin(Omega)
    cw, sw = np.cos(omega), np.sin(omega)

    R11, R12, R13 = co*cw - so*sw*ci, -co*sw - so*cw*ci, so*si
    R21, R22, R23 = so*cw + co*sw*ci, -so*sw + co*cw*ci, -co*si
    R31, R32, R33 = sw*si, cw*si, ci

    X = R11*xp + R12*yp
    Y = R21*xp + R22*yp
    Z = R31*xp + R32*yp

    return t, X, Y, Z

def plot_and_save(t, X, Y, Z, cfg):
    os.makedirs("output", exist_ok=True)
    
    # Save CSV
    with open("output/trajectory.csv", 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['time_s', 'X_m', 'Y_m', 'Z_m'])
        for ti, xi, yi, zi in zip(t, X, Y, Z):
            writer.writerow([ti, xi, yi, zi])

    # Plot 3D
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    
    r_e = cfg['constants']['r_earth']
    u = np.linspace(0, 2*np.pi, 40)
    v = np.linspace(0, np.pi, 40)
    xe = r_e * np.outer(np.cos(u), np.sin(v))
    ye = r_e * np.outer(np.sin(u), np.sin(v))
    ze = r_e * np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_surface(xe, ye, ze, color='lightblue', alpha=0.5, linewidth=0)

    ax.plot(X, Y, Z, 'b-', linewidth=2, label='Trajectory')
    ax.plot([X[0]], [Y[0]], [Z[0]], 'go', markersize=8, label='Epoch')
    
    ax.set_xlabel('X (m)'); ax.set_ylabel('Y (m)'); ax.set_zlabel('Z (m)')
    ax.set_title('Keplerian Orbit Propagation (ECI)')
    ax.legend()
    ax.set_box_aspect([1,1,1])
    plt.tight_layout()
    plt.savefig("output/orbit_plot.png", dpi=150)
    print("✅ Results saved to output/ folder.")

if __name__ == "__main__":
    print("🛰️ Starting orbit propagation...")
    cfg = load_config()
    t, X, Y, Z = propagate_orbit(cfg)
    plot_and_save(t, X, Y, Z, cfg)
    print("🎉 Done. Check output/trajectory.csv & output/orbit_plot.png")