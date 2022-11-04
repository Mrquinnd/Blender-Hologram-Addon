bl_info = {
    "name" : "Shader Library",
    "author" : "Quinn Dacre",
    "version" : (1,0),
    "blender" : (2,80,0),
    "location" : "View3d > Tool",
    "warning" : "",
    "wiki_url" : "",
    "category" : "Add Mesh",

}

import bpy



class ShaderMainPanel(bpy.types.Panel):
    bl_label = "Shader Library"
    bl_idname = "SHADER_PT_MAINPANEL"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Shader Library"

    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text="Select a Shader to be added.")
        row.operator('shader.diamond_operator', icon= 'DECORATE_ANIMATE')
        
      #text  
class SHADER_OT_DIAMOND(bpy.types.Operator):
     #Add the Diamond Shader to your selected Object.
    bl_label = "Diamond"
    bl_idname = "shader.diamond_operator"
    
def execute(self, context): 
       
    #Creating a new shader and calling it Diamond   
    material_diamond = bpy.data.materials.new(name="Diamond")
    material_diamond.use_nodes = True
    
    material_diamond.node_tree.nodes.remove(material_diamond.node_tree.nodes.get('Principled BSDF'))
        
    material_output =material_diamond.node_tree.nodes.get('material_output')
    material_output.location = (400, 0)
        

        #Glass material 1
    glass1_node = material_diamond.node_tree.nodes.new('ShaderNodeBsdfGlass')
        
    glass1_node.location = (-600,0)
        
    glass1.inputs[0].default_value = (0, 0.77624, 1, 1)

    glass1.inputs[2].default_value = 1.446
        
        
        #Glass material 2
    glass2_node = material_diamond.node_tree.nodes.new('ShaderNodeBsdfGlass')
        
    glass2_node.location = (-600,-150)
        
    glass2.inputs[0].default_value = (0, 0.77624, 0.3, 1)

    glass2.inputs[2].default_value = 1.450
        
        
         #Glass material 3
    glass3_node = material_diamond.node_tree.nodes.new('ShaderNodeBsdfGlass')
        
        #Sets location
    glass3_node.location = (-600,-150)
        
        #Sets values
    glass3.inputs[0].default_value = (0, 0, 1, 1)

        #Sets IOR
    glass3.inputs[2].default_value = 1.450
        
          #Glass material 4
    glass4_node = material_diamond.node_tree.nodes.new('ShaderNodeBsdfGlass')
        
        #Sets location
    glass4_node.location = (-600,-150)
        
        #Sets values
    glass4.inputs[0].default_value = (0, 0, 0, 0)

        #Sets IOR
    glass4.inputs[2].default_value = 1.450
        
        
        #Create the reference shader and reference as add 1
    add1_node = material_diamond.node_tree.nodes.new("ShaderNodeAddShader")
        
        #Setting the location
    add1_node.location(-500, -50)
        
        #Setting the label
    add1_node.label("Add1")
        
        #Minimises Nodes
    add1_node.hide = True
        
        #Deselects the node
    glass1_node.select = False
        
        
        #Create the reference shader and reference as add 1
    add2_node = material_diamond.node_tree.nodes.new("ShaderNodeAddShader")
        
        #Setting the location
    add2_node.location(-600, -50)
        
        #Setting the label
    add2_node.label("Add1")
        
        #Minimises Nodes
    add2_node.hide = True
        
        #Deselects the node
    glass2_node.select = False
        
        
    #Creating links
    material_diamond.node_tree.links.new(glass1_nodes[0], add1_node.inputs[0])
        
        
    material_diamond.node_tree.links.new(glass2_nodes[0], add1_node.inputs[1])
    material_diamond.node_tree.links.new(add1_node.outputs[0],add2_node.outputs[0])
        
        
    material_diamond.node_tree.links.new(glass3_node.outputs[0],add2_node.inputs[1])
        
    material_diamond.node_tree.links.new(add2_node.outputs[0],mix1_node.inputs[1])

    material_diamond.node_tree.links.new(glass4_node.outputs[0],mix1_node.inputs[2])

    material_diamond.node_tree.links.new(mix1_node.outputs[0],material_output.inputs[0])
       
    #Adding Material to the currently selected object
    bpy.context.object.active_material = material_diamond
       
    return {"FINISHED"}

    
def register():
    bpy.utils.register_class(ShaderMainPanel)
    bpy.utils.register_class(SHADER_OT_DIAMOND)

def unregister():
    bpy.utils.unregister_class(ShaderMainPanel)
    bpy.utils.unregister_class(SHADER_OT_DIAMOND)
    
if __name__ == "__main__":
    register()

