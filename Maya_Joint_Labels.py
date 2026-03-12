import maya.cmds as cmds
import maya.mel as mel

class SetJointsLabels:
    '''Sets joint labels as type "object" and uses its name as label, side set by left and right name
    :param left: left prefix/suffix in joint name to replace, sets left side by name
    :param right: right prefix/suffix in joint name to replace, sets right side by name
    :param hierarchy: if True selection and its children will be used'''
    def __init__(self,left='l_', right='r_', hierarchy=True):

        self.__left = left
        self.__right = right
        self.__hierarchy = hierarchy
        self.__selected = cmds.ls(sl=True)

    @property
    def selected(self):
        return self.__selected

    @property
    def left(self):
        return self.__left
    @property
    def right(self):
        return self.__right
    @property
    def hierarchy(self):
        return self.__hierarchy

    def selected_hierarchy(self):
        "get selection and its hierarchy"
        selection = self.selected
        selection_children = cmds.listRelatives(selection, type='joint', allDescendents=True)
        selection_hierarchy = selection + selection_children
        print(selection_hierarchy)
        return selection_hierarchy

    def set_selected(self):
        "sets selection based on hierarchy set to True or False"
        hierarchy = self.hierarchy
        if hierarchy is True:
            selection_to_label = self.selected_hierarchy()
        else:
            selection_to_label = self.selected
        return selection_to_label

    def label_joints(self):
        "label joints based on name"
        selected= self.set_selected()
        print(selected)
        left = self.left
        right = self.right
        TYPE=18 # sets type to "other"

        for s in selected:
            if left in s:
                label_name = s.replace(left, '')
                side = 1
            elif right in s:
                label_name = s.replace(right, '')
                side = 2
            else:
                label_name = s
                side = 0
            label_type_command = f'setAttr "{s}.type" {TYPE};'
            label_side_command = f'setAttr "{s}.side" {side};'
            label_name_command =  f'setAttr -type "string" {s}.otherType "{label_name}";'

            mel.eval(label_type_command)
            mel.eval(label_name_command)
            mel.eval(label_side_command)

set_labels = SetJointsLabels(left='l_', right='r_', hierarchy=True)
set_labels.label_joints()