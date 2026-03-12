# Maya Joint Labeling Python Script

Sets joint labels as type "object" and uses its name as the name of the label. The side set by left and right name parameter.
Must one joint selected to run.

# How to install

Open Maya.
Open script editor.
Open new tab and choose "python"
Copy and paste script to tab
Drag and drop script from tab to shelf to add to shelf

# How to Use

Select joint to change label of.
Run script.

# Set Parameters on line 73:

Can modify the parameters in paratheses at bottom of code
set_labels = SetJointsLabels(left='l_', right='r_', hierarchy=True)

left:  Left prefix/suffix in joint name to replace, sets left side by name. For other prefix/suffix, replace word in ''. Default is set to 'l_'.

right: Right prefix/suffix in joint name to replace, sets right side by name. For other prefix/suffix, replace word in ''. Default is set to 'r_'.

hierarchy: if True selection and its children will be used, replace True with False, to only label selection

## Troubleshooting

1. Make sure a joint is selected before running
2. if left and right side do not use "r_" and "l_" in naming, set names in parameter (Check Set Parameters on line 73 section)

##Licensing
###Made with no ai or vibe coding
Can use anywhere. Just credit original creator if used for commercial use.