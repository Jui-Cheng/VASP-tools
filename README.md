# Charge Density Slice Tool (CDST)

*********************************************************
CHARGE DENSITY SLICE TOOL (CDST) for VASP output files

This python program is produced by Jui-Cheng Kao

From Department of Materials Science and Engineering

National Yang Ming Chiao Tung University, Hsinchu, Taiwan

*********************************************************
Please feel free if users have any questions.

Email: jckao.en10@nycu.edu.tw

2023/03/21

*********************************************************

These tools are for the post-processing data of first-principles calculation package VASP.
The CHG_slice.py program is used to deal with the grid-based charge density information from VASP.
You have to responce four answers to the program.
First is the filename for charge density (CHGCAR, CHGDIFF.vasp, or PARCHG...).
Second, the z-position (angstrom) of the atomic model you want to slice.
Third and forth are the periodicity of x- and y-direction, respectively.

Example:

Please input the charge density filename: CHGCAR

Please input the z position you want to slice (crystal coordinate): 6.17

Please input the periodicity along x-direction: 3

Please input the periodicity along y-direction: 3


Then, you will get a fancy graphic of the 2D slice of charge density.
