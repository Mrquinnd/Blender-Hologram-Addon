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
        row.operator=('')
      
      #text  
class SHADER_OT_DIAMOND(bpy.types.Operator):
    bl_label = "Diamond"
    bl_idname = "shader.diamond_operator"
    
def execute(self, context): 
       
    #Creating a new shader and calling it Diamond   
    material_diamond = bpy.data.materials.new(name="Diamond")
    material_diamond.use_nodes = True
    
    
    material_diamond.node_tree.nodes.remove(material_diamond.node_tree.nodes.get('Principled BSDF'))
    
    material_output = material_diamond.node_tree.nodes.get('material_output')
    material_output.location = (400, 0)
    
    #Glass material 1
    glass1_node = material_diamond.node_tree.nodes.add('ShaderNodeBsdfGlass')
    
    glass1_node.location = (-600,0)
    
    glass1.inputs[0].default_value = (0, 0.77624, 1, 1)

    glass1.inputs[2].default_value = 1.446
    
    
    
def register():
    bpy.utils.register_class(ShaderMainPanel)

def unregister():
    bpy.utils.unregister_class(ShaderMainPanel)
    
if __name__ == "__main__":
    register()
