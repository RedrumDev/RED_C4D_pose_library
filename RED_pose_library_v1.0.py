
import c4d

ctrl_prefix = ""
ctrl_list =""
char_name = ""
pose_folder = ""




def initiate_ui():
    pass

def initiate_character():
    pass
    
def generate_thumbnail():
    pass

def generate_folder():
    psdd
    
def generate_fbx_pose():
    pass
    
def add_pose():
    pass
              
     


initiate_ui()







"""
Pseudo Code
Step 1 Initiate the user interface


Step 2
After the user clicks on the button "Iniate a T-pose of your character"
The tool...
A) Grabs the selected root_object of your character (it will include geoetry and controlelrs)
B) The tool will first ask "what is your current controllers prefix?".... for example "CTRL"
C) The tool will ask "give your character a name"
D) The tool will ask "In what folder do you wish to store your "character name naam" library?


Functions:
After initializing the character
F1) Generates the folder + exports a 1 frame FBX inclusing keyframes that are set on the current frame
F2) It will store a thumbnail (T-pose) of your character
F3) It will add that thumbnail to the library UI panel


Step 3
When the user clicks on "add pose"
Grabs the selected root_object of your character (it will include geoetry and controllers). And it stores that pose based on the Controllers keyframes on the current frame.


Step 5 (using poses)
When a user clicks on a thmbnail, it promps if you want to use that pose on the current frame on your chatacter.
(test - if there is a mismatch in controlelrs-count it will prompt an error)


"""