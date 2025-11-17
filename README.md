<p align="center">
    <img src=".assets/img/icon_512.png" alt="Project Icon" width="150">
    <br>
    <h1 align="center">
        Analog Computing Elements for LTspice
    </h1>
    <h3 align="center">
        A library of archetypal analog computing elements for rapid analog circuit prototyping in LTspice.
    </h3>
    <p></p>
    <p align="center">
    <a href="#about">About</a> •
    <a href="#key-features">Key Features</a> •
    <a href="#quick-start">Quick Start</a> •
    <a href="#learn-more">Learn More</a>
    </p>
    <p></p>
</p>

<br>

<picture>
    <source media="(prefers-color-scheme: dark)" srcset=".assets/img/computing_element_symbols/all_elements_white.svg">
    <source media="(prefers-color-scheme: light)" srcset=".assets/img/computing_element_symbols/all_elements_black.svg">
    <img src=".assets/img/computing_element_symbols/all_elements_black.svg" alt="Banner">
</picture>

<br>

<p align="center">
    <img src=".assets/img/oscillator.gif" alt="Usage Example" width="600">
    <br>
    Adding a summer element to complete an analog circuit for a simple one-dimensional oscillator.
</p>

## About

This library provides a complete set of LTspice-compatible analog computing elements – integrators, summers, multipliers, dividers, log/antilog blocks, and more – packaged as reusable components.
Instead of hand-drawing op-amp circuits and updating values by hand, you work with high-level computing primitives that are parameterised via SPICE directives and designed for hierarchical, modular analog computing systems.

The elements are available at three abstraction levels (numerical, ideal-component, and real-component), letting you move smoothly from pure mathematical models to realistic circuit implementations using actual SPICE device models.

## Key Features

- **Complete element set** – Integrators, summers, multipliers, dividers, log/antilog, differentiators, buffers, and more
- **Three simulation levels** – Numerical, ideal-component, and real-component implementations for different design stages
- **Parameterised design** – Configure behaviour using SPICE parameters (e.g., time constants, gains, scaling factors)
- **Hierarchical and modular** – Build complex systems from reusable computing subcircuits
- **Batch and scripting friendly** – Works well with LTspice batch modes and tools like PyLTSpice
- **Cross‑platform** – Compatible with any platform that runs LTspice

## Quick Start

1. Clone or download this repository.
2. Run the make script: `./make.py` or `python3 make.py`.
3. Copy the contents of the generated `all` directory into your LTspice project directory.
4. In LTspice, open (or create) a schematic and press `F2` to open the component picker.
5. Set your project directory as the top directory and place the desired computing elements.
6. Wire elements together and add SPICE directives (e.g. `.tran`) as you would in any LTspice schematic.

For example schematics demonstrating all elements, and for detailed installation notes (including Windows-wide installation), see **[DOCUMENTATION.md](DOCUMENTATION.md)**.

## Learn More

For full documentation, including:

- Detailed descriptions of each computing element and its transfer function
- Explanations of the numerical / ideal / real simulation types
- Example circuits (testbench and simple oscillator)
- Parameterisation and simulation tips
- Troubleshooting guidance for convergence and timestep issues

See **[DOCUMENTATION.md](DOCUMENTATION.md)**.

## Status

This project is stable but not under active development. It may receive occasional updates (for example, additional computing elements) but there are no concrete plans.

## License

This project is licensed under the [CC BY-NC-SA 4.0 License](https://creativecommons.org/licenses/by-nc-sa/4.0/).
