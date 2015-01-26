# Genome-Data-Parser

This repository is dedicated to the design and construction of a genomic data parser for the Tublitz Neuroscience lab at the University of Oregon. All of the actual genomic data is kept private.

Utilizes:
* <b>Pandas</b> and <b>Xlrd</b> module for handling csv, xls, and xlsx data
* <b>tkinter</b> for GUI creation
* <b>Matplotlib</b> for statistical representations
* <b>Py2exe</b> for executable construction

Features:
* Works with all csv/xls/xlsx data files
* Search across all column rows by keyword, including rows containing sub-arrays (separated by ;)
* Refine data through additional searches across columns
* Pie-chart output for representations of data composition
* Output final data as spreadsheet in auto-dated folders with user save names

The end goal is a multifaceted interface for combing through very large sets of data with optional visuals describing terms of interest.
