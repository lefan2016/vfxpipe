import maya.cmds as cmds
import maya.utils as utils
import maya.mel as mel
import os, sys

def setupMayaPipe():

    import fxpipe # generic and should already be loaded!
    import vrayUtils # for vray mojo

    # let's create the menus
    if cmds.menu('fxpipeMenu', exists=1):
        cmds.deleteUI('fxpipeMenu')

    fxpipeMenu = cmds.menu('fxpipeMenu', p='MayaWindow', to=1, aob=1, l='fxPipeline')
    jobMenu = cmds.menuItem('jobMenu', p=fxpipeMenu, subMenu = 1, l="Jobs")
    cmds.menuItem(p=fxpipeMenu, d=1)
    toolsMenu = cmds.menuItem(p=fxpipeMenu, subMenu = 1, l="Tools")
    vrayMenu = cmds.menuItem(p=toolsMenu, subMenu = 1, l='VRay')
    
    # Tools Menu
    
    # VRay Menu
    # please note that even though we have imported vrayUtils, we need to do it again in the commands as it loses context.
    cmds.menuItem(p=vrayMenu, l='Set up basic render settings', c='import vrayUtils;vrayUtils.createBaseRenderSettings()')
    cmds.menuItem(p=vrayMenu, l='Add Gamma to file nodes', c='import vrayUtils;vrayUtils.vrayAddGamma()')
    cmds.menuItem(p=vrayMenu, l='Add tech render passes', c='import vrayUtils;vrayUtils.createTechPasses()')
    cmds.menuItem(p=vrayMenu, l='Add Light Select Render Element', c='import vrayUtils;vrayUtils.createLightSelect()')
    
    
    if fxpipe.job != '':
        mayaJobPath = (os.path.join(fxpipe.jobPath, fxpipe.job, fxpipe.jobPathMaya))
        sys.path.append(mayaJobPath)
    
       
    

utils.executeDeferred('setupMayaPipe()') # wait until maya is ready to do the real work here...