F1 Racing Line Generator & Lap Simulation Tool

A Python-based system for generating smooth racing lines from F1 track data and simulating complete lap dynamics.
This project reconstructs circuits using spline interpolation, computes curvature and vehicle physics, and will eventually support real-time visualization of forces, acceleration, and car motion through a custom UI.

🚀 Features
✔ Track Geometry Engine

Load track point data from CSV files

Generate smooth parametric splines for X(t) and Y(t)

Sample 1000–10,000 points for plotting and physics

Visualize circuits with Seaborn/Matplotlib

✔ Physics-Driven Lap Simulation (coming soon)

Curvature calculation along the spline

Maximum cornering speeds based on physics

Braking & acceleration modeling

Downforce, drag, tire force simulation

✔ Racing Line Optimization (future update)

Generate optimal lines within track boundaries

Provide error feedback when a line cannot be computed

✔ Real-Time UI (future update)

Display car moving along the racing line

Show real-time force vectors (lateral, longitudinal, downforce, etc.)

Speed vs distance graphs

Braking zones, apex detection, etc.

🧩 Project Structure
F1-racing-line-simulator/
│
├── main.py
├── requirements.txt
├── .gitignore
│
├── geometry/
│ ├── track_loader.py
│ ├── spline_generator.py
│ └── curvature.py (coming soon)
│
├── physics/
│ ├── acceleration.py
│ ├── braking.py
│ ├── aerodynamics.py
│ └── tire_model.py
│
├── simulation/
│ ├── lap_simulator.py
│ └── optimizer.py
│
├── ui/
│ ├── plotter.py
│ └── (future UI files)
│
└── data/
└── tracks/
├── monza.csv
├── suzuka.csv
├── spa.csv
├── silverstone.csv
└── sakhir.csv

📊 Example Output

(Add your Monza plot here later)

# Example code used to generate the plot:

x, y = load_track("monza")
sx, sy, t = generate_spline(x, y)
xv, yv, tv = evaluate_spline(sx, sy, 2000)

🛠 Installation

1. Clone the repository
   git clone https://github.com/captainducki/F1-racing-line-simulator.git
   cd F1-racing-line-simulator

2. Create & activate virtual environment
   python -m venv f1sim
   f1sim\Scripts\activate # Windows
   source f1sim/bin/activate # Mac/Linux

3. Install dependencies
   pip install -r requirements.txt

📈 Roadmap
Phase 1 — Geometry Engine (In Progress)

CSV track loading ✔

Spline generation ✔

Plotting & visualization ✔

Track normalization (coming)

Phase 2 — Physics Engine

Curvature computation

Longitudinal forces

Lateral grip / downforce model

Acceleration & braking curves

Phase 3 — Racing Line Optimization

Boundary-aware trajectory generation

Error feedback system

Time-minimizing racing lines

Phase 4 — User Interface

Real-time car animation

Force vector visualization

Speed/force graphs

📄 License

This project uses the MIT License.

🤝 Contributing

Contributions are welcome — open an issue or create a pull request.

⭐ Acknowledgements

Track CSV files sourced from the open-source TUMFTM Track Database on GitHub.
