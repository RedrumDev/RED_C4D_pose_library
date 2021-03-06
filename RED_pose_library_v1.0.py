
import c4d
from c4d import gui
import re  # Regular expression
import json



plugin_ID = 1054468
Associated_Label = "RED_pose_library"

ctrl_prefix = ""
ctrl_list =""
ctrl_list_size = ""
char_name = ""
pose_folder = ""
pose_name = ""
pose_folder = "C:\Redrum programming\RED_pose_library_test_folder"

pose_data = {}

ctrl_prefix = c4d.gui.InputDialog("What is your controllers pefix?", "CTRL")
pose_name = c4d.gui.InputDialog("What is the name of your current pose?", "")
save_folder = c4d.storage.SaveDialog(title="Stores Poses", force_suffix="", def_path="", def_file=pose_name)

print ctrl_prefix


# get current keyframe
def GetCurrentFrame():
    """
    This function returns the current frame taking onto account the project settings FPS value
    """
    projFPS = doc[c4d.DOCUMENT_FPS]
    curTime = doc.GetTime()
    curFrame = curTime.GetFrame(projFPS)
    # print "current frame is: ",  curFrame
    return curFrame

GetCurrentFrame()

# get the name of my surrect selected object
MySelected = doc.GetActiveObjects(0)
for myObject in MySelected:
    myObjectName =  myObject [c4d.ID_BASELIST_NAME]


# Grabs all my objects including its children, warns is nothig is selected, returns all objects
def objectChildren():
    def GetObjects(obj):
          objList = [obj]
          for kid in obj.GetChildren():
              objList += GetObjects(kid)
          return objList #return the selected object plus chidlren

    if  len(MySelected) <= 0:
        gui.MessageDialog('Your selection is empty, please select the root object of your character)')

    else:
        test = doc.SearchObject(myObjectName)
        myObjects = GetObjects(test)
        return myObjects

print "total objects is:", len(objectChildren())


#stores all objects where the name has a certain prefix in a list
for index, items in enumerate(objectChildren()):
    #json_waarde = {index:items}
    #y = json.dumps(json_waarde)
    #print y
    pass

    #print items[c4d.ID_BASELIST_NAME]

# Filter enkel CTRL* objecten


# gets the value of all keyframed COTROLLER attributes
trs = op.GetCTracks()
#if trs != None:
for tr in objectChildren():
        #if tr.GetDescriptionID()[0].id == c4d.ID_BASEOBJECT_POSITION:
        #    if tr.GetDescriptionID()[1].id == c4d.VECTOR_X:
        #        trpX = tr
        tracked = tr.GetCTracks()
        print tr
        for track in tracked:
            myCurve = track.GetCurve()
            keyframe_waarde = myCurve.GetValue(c4d.BaseTime(GetCurrentFrame()),)
            print keyframe_waarde
            print track
            print track[c4d.ID_BASELIST_NAME]
            #pass

        #print trackedAttributes[c4d.ID_BASELIST_NAME]


def render_thumbnail():
     # Retrieves the current active render settings
    rd = doc.GetActiveRenderData()
    print rd
    
    renderpath = "C:\Redrum programming\RED_pose_library_test_folder\naam"
    
    #doc.GetActiveRenderData()[c4d.RDATA_PATH] = "C:\Redrum programming\RED_pose_library_test_folder\RED_pose_library_test_folder"
    doc.GetActiveRenderData()[c4d.RDATA_PATH] = save_folder
    doc.GetActiveRenderData()[c4d.RDATA_FRAMESEQUENCE] = 1

    
    saved = rd[c4d.RDATA_RENDERENGINE] 
    rd[c4d.RDATA_RENDERENGINE]  = c4d.RDATA_RENDERENGINE_PREVIEWHARDWARE

    # Creates a Multi Pass Bitmaps that will store the render result
    bmp = c4d.bitmaps.MultipassBitmap(int(rd[c4d.RDATA_XRES]), int(rd[c4d.RDATA_YRES]), c4d.COLORMODE_RGB)
    if bmp is None:
        raise RuntimeError("Failed to create the bitmap.")


    # Adds an alpha channel
    bmp.AddChannel(True, True)

    # Renders the document
    if c4d.documents.RenderDocument(doc, rd.GetData(), bmp, c4d.RENDERFLAGS_EXTERNAL) != c4d.RENDERRESULT_OK:
        raise RuntimeError("Failed to render the temporary document.")

    # Displays the render in the Picture Viewer
    #c4d.bitmaps.ShowBitmap(bmp)

    rd[c4d.RDATA_RENDERENGINE] = saved


render_thumbnail()

# Hoe data op te slaan
# controllers = {object[],objectnaam[],waarde,curve}


# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)






# the result is a Python dictionary:
#print(y["age"])



#track = op.FindCTrack(descid)
#>
#>     curve = track.GetCurve()
# for i in xrange(100) :
#>
#>         x = i / 99.0
#>
#>         print curve.GetValue(c4d.BaseTime(x), fps)




"""
TODO:

A Get Active Object Name


A) get all children of teh slected object
B) If the name of the children contains "CTRL*" then store those objects in a list
C) Store the lengt of the list as a variable (in order to match length and error check during future use)
"""




# Get the selected objects, including children.
selection = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_CHILDREN)
#print selection

#print op()



#if len(selection) <= 0:
#        gui.MessageDialog('Your selection is empty, please select the root object of your character)')




"""
def GetObjectKeyframes():
    obj = doc.GetActiveObject()
    print obj

    hasKeyframes = objFindCtrack()

GetObjectKeyframes()
"""


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





# Unique id numbers for each of the GUI elements
LBL_USAGE = 1000
LBL_INFO1 = 1001
LBL_INFO2 = 1002
GROUP_TEXT = 10000
TXT_FIND = 10001
TXT_REPLACE = 10002
CHK_MATCH_CASE = 10003
GROUP_OPTIONS = 20000
BTN_OK = 20001
BTN_CANCEL = 20002

class OptionsDialog(gui.GeDialog):
  """ Dialog for doing a find replace on object names.
  """
  def CreateLayout(self):
    self.SetTitle('Find and Replace Object Names')
    self.AddMultiLineEditText(LBL_USAGE, c4d.BFH_SCALEFIT, inith=40, initw=500,
                              style=c4d.DR_MULTILINE_READONLY)
    self.SetString(LBL_USAGE,
        "USAGE: Does find/replace on selected object names\n"
        "   using regular expression")
    # Find replace strings:
    self.GroupBegin(GROUP_TEXT, c4d.BFH_SCALEFIT, 2, 2)
    self.AddStaticText(LBL_INFO1, c4d.BFH_LEFT, name='Find:')
    self.AddEditText(TXT_FIND, c4d.BFH_SCALEFIT)
    self.SetString(TXT_FIND, 'Cap1')
    self.AddStaticText(LBL_INFO2, c4d.BFH_LEFT, name='Replace with:')
    self.AddEditText(TXT_REPLACE, c4d.BFH_SCALEFIT)
    self.SetString(TXT_REPLACE, 'Floor')
    self.GroupEnd()
    self.AddSeparatorH(c4d.BFH_SCALE);
    # Checkbox Option - append to existing string:
    self.AddCheckbox(CHK_MATCH_CASE, c4d.BFH_SCALEFIT,
                     initw=1, inith=1, name="match case")
    self.SetBool(CHK_MATCH_CASE, True)
    self.AddSeparatorH(c4d.BFH_SCALE);
    # Buttons - an Ok and Cancel button:
    self.GroupBegin(GROUP_OPTIONS, c4d.BFH_CENTER, 2, 1)
    self.AddButton(BTN_OK, c4d.BFH_SCALE, name='OK')
    self.AddButton(BTN_CANCEL, c4d.BFH_SCALE, name='Cancel')
    self.GroupEnd()
    self.ok = False
    return True

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