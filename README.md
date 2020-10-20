# Toy Kiva Robot

## Overview

The Kiva System is a solution for storing, moving, and sorting inventory used in Warehouses and Distribution Centers to improve worker productivity. The products are stored in pods and Kiva robots are used to carrying them between storage location and drop zone (D’Andrea, Wurman, 2008; Wurman, D’Andrea, Mountz, 2008).

In this project, we will code a Remote Control which commands Kiva Robot to move, take and drop pods.

## Goals

Create a Remote Control that provides a map with obstacles, Kiva Robot (K), take (T), and drop (D) zone area. The user should provide a path that successfully picks up and drops off the pod. In order to control a Kiva, it sends a simple string of letters of commands:

- 'F': move kiva one step forward, and keeping the facing direction;
- 'L': turn kiva 90 degrees to its left;
- 'R': turn kiva 90 degrees to its right;
- 'T': take the pod;
- 'D': drop the pod;

## References

```
@inproceedings{
    2008_DAndrea_Wurman,
    year={2008},
    author={D’Andrea, Raffaello and Wurman, Peter R.}
    title={Future challenges of coordinating hundreds of autonomous vehicles in distribution facilities},
    url={https://ieeexplore.ieee.org/document/4686677},
    doi={10.1109/TEPRA.2008.4686677},
    booktitle={2008 IEEE International Conference on Technologies for Practical Robot Applications},
    pages={80-83}
}
```
```
@article{
    2008_Wurman_DAndrea_Mountz,
    year={2008},
    author={Wurman, Peter R. and D’Andrea, Raffaello and Mountz, Mick},
    title={Coordinating Hundreds of Cooperative, Autonomous Vehicles in Warehouses},
    url={https://www.aaai.org/ojs/index.php/aimagazine/article/view/2082},
    DOI={10.1609/aimag.v29i1.2082},
    journal={AI Magazine},
    volume={29},
    number={1},
    month={Mar.},
    pages={9-20}
}
```
