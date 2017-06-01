# MaxPlus.py for 3dsMax 2015 Python IDE emulator
# Version : 1.0
# Author: jintaeks@gmail.com
# Date: jintaeks on 2017-06-01_20-53

# dummy classes for return or parameter types
# TimeValue is not defined in 'MaxPlus'
# jintaeks on 2017-06-01_21-43
class TimeValue:
    pass

class DWORD:
    pass

class ULONG:
    pass

class COLORREF:
    pass

class SClass_ID:
    pass

class ParamID:
    pass

class ParamType2:
    pass

####################################################################################################
# MaxPlus classes
class _CustomActionItem:
    pass


class _INTERNAL_CustomActionCallback:
    pass


class _INTERNAL_NotificationManager:
    pass


class _NotificationHandler:
    pass


class _object:
    pass


class _static_generator_property:
    pass


class AbstractCustomActionItem:
    this = ()
    def Execute(self):
        pass

    def GetButtonText(self):
        pass

    def GetCategoryText(self):
        pass

    def GetDescription(self):
        pass

    def GetId(self):
        pass

    def GetMenuText(self):
        pass

    def IsChecked(self):
        pass

    def IsEnabled(self):
        pass

    def IsIndeterminate(self):
        pass

    def IsVisible(self):
        pass


class AbstractNotificationHandler:
    this = ()
    def OnNotify(self):
        pass


class Wrapper:
    def GetUnwrappedPtr(self):
        pass


class InterfaceServer(Wrapper):
    def GetInterface(self):
        pass


class Animatable(InterfaceServer):
    AnimHandle = ()
    ClassID = ()
    ClearFlagInAllAnimatables = ()
    GetAnimByHandle = ()
    KeyTimes = ()
    NodeName = ()
    NumSubAnims = ()
    ParameterBlock = ParameterBlock()
    SubAnimNames = ()
    SubAnims = ()
    SuperClassID = ()

    def AddNewKey(self):
        pass

    def AssignController(self):
        pass

    def CanAssignController(self):
        pass

    def CanCopyAnim(self):
        pass

    def CanCopyTrack(self):
        pass

    def CanDeleteSubAnim(self):
        pass

    def CanMakeUnique(self):
        pass

    def ClearAFlag(self):
        pass

    def ClearAFlagEx(self):
        pass

    def ClearFlagBit(self):
        pass

    def ClearFlagInAllAnimatables(self):
        pass

    def CopyKeysFromTime(self):
        pass

    def DeleteKeyAtTime(self):
        pass

    def DeleteKeyByIndex(self):
        pass

    def DeleteKeys(self):
        pass

    def DeleteSubAnim(self):
        pass

    def DeleteTime(self):
        pass

    def DoesSupportTimeOperations(self):
        pass

    def EditTimeRange(self):
        pass

    def FreeCaches(self):
        pass

    def GetAnimByHandle(self):
        pass

    def GetAnimHandle(self):
        pass

    def GetClassID(self):
        pass

    def GetClassName(self):
        pass

    def GetCustomAttributeContainer(self):
        pass

    def GetHasSubElements(self):
        pass

    def GetKeyIndex(self):
        pass

    def GetKeyTime(self):
        pass

    def GetNextKeyTime(self):
        pass

    def GetNodeName(self):
        pass

    def GetNumKeys(self):
        pass

    def GetNumSubAnims(self):
        pass

    def GetParameterBlock(self):
        pass

    def GetSubAnim(self):
        pass

    def GetSubAnimName(self):
        pass

    def GetSuperClassID(self):
        pass

    def GetTimeRange(self):
        pass

    def InsertTime(self):
        pass

    def IsAnimated(self):
        pass

    def IsKeyAtTime(self):
        pass

    def IsSubClassOf(self):
        pass

    def MoveKeys(self):
        pass

    def ReverseTime(self):
        pass

    def ScaleKeyValues(self):
        pass

    def ScaleTime(self):
        pass

    def SetAFlag(self):
        pass

    def SetAFlagEx(self):
        pass

    def SetFlagBit(self):
        pass

    def SubNumToRefNum(self):
        pass

    def TestAFlag(self):
        pass

    def TestAFlagEx(self):
        pass

    def TestFlagBit(self):
        pass


class BaseInterface(InterfaceServer):
    Id = ()
    def GetID(self):
        pass


class BaseInterfaceServer(InterfaceServer):
    Interface = ()
    NumInterfaces = ()

    def GetInterfaceAt(self):
        pass

    def GetNumInterfaces(self):
        pass


class ICustomControl(InterfaceServer):
    Enabled = ()
    Hwnd = ()

    def Enable(self):
        pass

    def GetHwnd(self):
        pass

    def IsEnabled(self):
        pass


class Viewport(InterfaceServer):
    def CommitImplicitGrid(self):
        pass

    def GetAdaptiveDegCameraDistancePriority(self):
        pass

    def GetAdaptiveDegDegradeLight(self):
        pass

    def GetAdaptiveDegDisplayModeBox(self):
        pass

    def GetAdaptiveDegDisplayModeCurrent(self):
        pass

    def GetAdaptiveDegDisplayModeFastShaded(self):
        pass

    def GetAdaptiveDegDisplayModeHide(self):
        pass

    def GetAdaptiveDegDisplayModePoint(self):
        pass

    def GetAdaptiveDegDisplayModeWire(self):
        pass

    def GetAdaptiveDegDrawBackface(self):
        pass

    def GetAdaptiveDegGoalFPS(self):
        pass

    def GetAdaptiveDegMinSize(self):
        pass

    def GetAdaptiveDegNeverDegradeSelected(self):
        pass

    def GetAdaptiveDegNeverRedrawAfterDegrade(self):
        pass

    def GetAdaptiveDegScreenSizePriority(self):
        pass

    def GetBkgImageDsp(self):
        pass

    def GetConstructionTM(self):
        pass

    def GetCPDisp(self):
        pass

    def GetDamageRect(self):
        pass

    def GetDIB(self):
        pass

    def GetEdgedFaces(self):
        pass

    def GetFocalDist(self):
        pass

    def GetFOV(self):
        pass

    def GetFPS(self):
        pass

    def GetGridSize(self):
        pass

    def GetGridType(self):
        pass

    def GetHither(self):
        pass

    def GetHWnd(self):
        pass

    def GetPointOnCP(self):
        pass

    def GetScreenScaleFactor(self):
        pass

    def GetSFDisplay(self):
        pass

    def GetSingleDefaultLight(self):
        pass

    def GetViewCamera(self):
        pass

    def GetViewMatrix(self):
        pass

    def GetViewportClipScale(self):
        pass

    def GetViewportFPS(self):
        pass

    def GetViewSpot(self):
        pass

    def GetViewType(self):
        pass

    def GetVPWorldWidth(self):
        pass

    def GetYon(self):
        pass

    def GetZoom(self):
        pass

    def Invalidate(self):
        pass

    def InvalidateRect(self):
        pass

    def IsActive(self):
        pass

    def IsDegrading(self):
        pass

    def IsEnabled(self):
        pass

    def IsGridVisible(self):
        pass

    def IsPerspView(self):
        pass

    def IsValid(self):
        pass

    def IsWire(self):
        pass

    def MapCPToWorld(self):
        pass

    def MapScreenToView(self):
        pass

    def MapScreenToWorldRay(self):
        pass

    def NonScalingObjectSize(self):
        pass

    def Pan(self):
        pass

    def ReleaseImplicitGrid(self):
        pass

    def Rotate(self):
        pass

    def SetAdaptiveDegCameraDistancePriority(self):
        pass

    def SetAdaptiveDegDegradeLight(self):
        pass

    def SetAdaptiveDegDisplayModeBox(self):
        pass

    def SetAdaptiveDegDisplayModeCurrent(self):
        pass

    def SetAdaptiveDegDisplayModeFastShaded(self):
        pass

    def SetAdaptiveDegDisplayModeHide(self):
        pass

    def SetAdaptiveDegDisplayModePoint(self):
        pass

    def SetAdaptiveDegDisplayModeWire(self):
        pass

    def SetAdaptiveDegDrawBackface(self):
        pass

    def SetAdaptiveDegGoalFPS(self):
        pass

    def SetAdaptiveDegMinSize(self):
        pass

    def SetAdaptiveDegNeverDegradeSelected(self):
        pass

    def SetAdaptiveDegNeverRedrawAfterDegrade(self):
        pass

    def SetAdaptiveDegScreenSizePriority(self):
        pass

    def SetBkgImageDsp(self):
        pass

    def SetEdgedFaces(self):
        pass

    def SetFocalDist(self):
        pass

    def SetFocalDistance(self):
        pass

    def SetFOV(self):
        pass

    def SetGridSize(self):
        pass

    def SetSFDisplay(self):
        pass

    def SetViewCamera(self):
        pass

    def SetViewMatrix(self):
        pass

    def SetViewportClipScale(self):
        pass

    def SetViewSpot(self):
        pass

    def SetViewUser(self):
        pass

    def SnapLength(self):
        pass

    def SnapPoint(self):
        pass

    def SnapPreview(self):
        pass

    def TrackImplicitGrid(self):
        pass

    def UndoAccept(self):
        pass

    def UndoBegin(self):
        pass

    def UpdateLabel(self):
        pass

    def Zoom(self):
        pass


class ReferenceMaker(Animatable):
    NumRefs = ()
    Refs = ()
    def ClearFlagInHierarchy(self):
        pass

    def DeleteMe(self):
        pass

    def DeleteReference(self):
        pass

    def FindRef(self):
        pass

    def GetNumRefs(self):
        pass

    def GetReference(self):
        pass

    def NotifyChanged(self):
        pass

    def NotifyDependents(self):
        pass

    def ReplaceReference(self):
        pass

    def RescaleWorldUnits(self):
        pass


class FPInterface(BaseInterface):
    def EnableActions(self):
        pass

    def FindFn(self):
        pass

    def GetDesc(self):
        pass

    def Invoke(self):
        pass

    def IsChecked(self):
        pass

    def IsEnabled(self):
        pass

    def IsVisible(self):
        pass


class BezierShape(BaseInterfaceServer):
    def AddAndWeld(self):
        pass

    def Append(self):
        pass

    def BindKnot(self):
        pass

    def BuildBoundingBox(self):
        pass

    def ClearDispFlag(self):
        pass

    def CloneSelectedParts(self):
        pass

    def CopyFrom(self):
        pass

    def CopyShapeDataFrom(self):
        pass

    def DeepCopy(self):
        pass

    def DeleteSelectedPolys(self):
        pass

    def DeleteSelectedSegs(self):
        pass

    def DeleteSelectedVerts(self):
        pass

    def DeleteSelSegs(self):
        pass

    def DeleteSelVerts(self):
        pass

    def DeleteSpline(self):
        pass

    def FreeChannels(self):
        pass

    def GetAffectBackface(self):
        pass

    def GetBoundingBox(self):
        pass

    def GetBubble(self):
        pass

    def GetClosures(self):
        pass

    def GetDeformBBox(self):
        pass

    def GetDispFlag(self):
        pass

    def GetEdgeDist(self):
        pass

    def GetFalloff(self):
        pass

    def GetKnotIndex(self):
        pass

    def GetLengthOfCurve(self):
        pass

    def GetMatID(self):
        pass

    def GetNumSegs(self):
        pass

    def GetNumSplines(self):
        pass

    def GetNumVerts(self):
        pass

    def GetOptimize(self):
        pass

    def GetPinch(self):
        pass

    def GetPolyAndKnot(self):
        pass

    def GetPolyAndVert(self):
        pass

    def GetReadyPatchCap(self):
        pass

    def GetSteps(self):
        pass

    def GetTopology(self):
        pass

    def GetTotalKnots(self):
        pass

    def GetTotalVerts(self):
        pass

    def GetUseEdgeDists(self):
        pass

    def GetUseSoftSelections(self):
        pass

    def GetVert(self):
        pass

    def GetVertexWeight(self):
        pass

    def GetVertIndex(self):
        pass

    def HideSelectedSegs(self):
        pass

    def HideSelectedSplines(self):
        pass

    def HideSelectedVerts(self):
        pass

    def Init(self):
        pass

    def InterpCurve3D(self):
        pass

    def InterpPiece3D(self):
        pass

    def InvalidateVertexWeights(self):
        pass

    def IsVertexWeightSupported(self):
        pass

    def MakeFirst(self):
        pass

    def MakePolyShape(self):
        pass

    def NewAndCopyChannels(self):
        pass

    def NewShape(self):
        pass

    def PrepKnotBaseIndex(self):
        pass

    def PrepVertBaseIndex(self):
        pass

    def ReadyCachedPolyShape(self):
        pass

    def RecordTopologyTags(self):
        pass

    def Reverse(self):
        pass

    def SelSegsSameType(self):
        pass

    def SelSplinesSameType(self):
        pass

    def SelVertsSameType(self):
        pass

    def SetAffectBackface(self):
        pass

    def SetBubble(self):
        pass

    def SetClosures(self):
        pass

    def SetDispFlag(self):
        pass

    def SetEdgeDist(self):
        pass

    def SetFalloff(self):
        pass

    def SetOptimize(self):
        pass

    def SetPinch(self):
        pass

    def SetSteps(self):
        pass

    def SetSupportVSelectionWeights(self):
        pass

    def SetUseEdgeDists(self):
        pass

    def SetUseSoftSelections(self):
        pass

    def SetVert(self):
        pass

    def SetVertexWeight(self):
        pass

    def SetVertexWeightCount(self):
        pass

    def ShallowCopy(self):
        pass

    def TangentCurve3D(self):
        pass

    def TangentPiece3D(self):
        pass

    def Transform(self):
        pass

    def UnbindKnot(self):
        pass

    def UnhideSegs(self):
        pass

    def UnselectHiddenSegs(self):
        pass

    def UnselectHiddenSplines(self):
        pass

    def UnselectHiddenVerts(self):
        pass

    def UpdateBindList(self):
        pass

    def UpdateEdgeDists(self):
        pass

    def UpdateSels(self):
        pass

    def UpdateVertexDists(self):
        pass

    def UpdateVertexWeights(self):
        pass

    def VertexFlagSel(self):
        pass

    def VertexTempSel(self):
        pass

    def VertexTempSelAll(self):
        pass


class Bitmap(BaseInterfaceServer):
    ClampColor = ()
    ClampColorA = ()
    ScaleColor = ()
    ScaleColorA = ()
    def ChannelsPresent(self):
        pass

    def ClampColor(self):
        pass

    def ClampColorA(self):
        pass

    def ClampScaleColor(self):
        pass

    def ClampScaleColorA(self):
        pass

    def ClearFlag(self):
        pass

    def Close(self):
        pass

    def CloseAll(self):
        pass

    def CopyImage(self):
        pass

    def CreateChannels(self):
        pass

    def CropImage(self):
        pass

    def DeleteChannels(self):
        pass

    def DeleteStorage(self):
        pass

    def DeleteThis(self):
        pass

    def Display(self):
        pass

    def Fill(self):
        pass

    def FromDib(self):
        pass

    def GetAspect(self):
        pass

    def GetFlags(self):
        pass

    def GetGamma(self):
        pass

    def GetHasFilter(self):
        pass

    def GetHeight(self):
        pass

    def GetMaxAlphaLevel(self):
        pass

    def GetMaxRGBLevel(self):
        pass

    def GetModifyID(self):
        pass

    def GetScaleColors(self):
        pass

    def GetStorage(self):
        pass

    def GetWidth(self):
        pass

    def GetWindow(self):
        pass

    def GoTo(self):
        pass

    def HasAlpha(self):
        pass

    def HasPreMultipliedAlpha(self):
        pass

    def IncrModifyID(self):
        pass

    def IsDithered(self):
        pass

    def IsHighDynamicRange(self):
        pass

    def IsPaletted(self):
        pass

    def OpenOutput(self):
        pass

    def Print(self):
        pass

    def ScaleColor(self):
        pass

    def ScaleColorA(self):
        pass

    def SetCroppingValues(self):
        pass

    def SetDither(self):
        pass

    def SetFilter(self):
        pass

    def SetFlag(self):
        pass

    def SetModifyID(self):
        pass

    def SetScaleColors(self):
        pass

    def SetStorage(self):
        pass

    def ShowProgressLine(self):
        pass

    def ToDib(self):
        pass

    def ToggleFlag(self):
        pass

    def UnDisplay(self):
        pass

    def Write(self):
        pass

    def WriteAll(self):
        pass


class BitmapStorage(BaseInterfaceServer):
    ClampColor = ()

    ClampColorA = ()

    ScaleColor = ()

    ScaleColorA = ()

    def Allocate(self):
        pass

    def AreChannelsPresent(self):
        pass

    def ClampColor(self):
        pass

    def ClampColorA(self):
        pass

    def ClampScaleColor(self):
        pass

    def ClampScaleColorA(self):
        pass

    def ClearFlags(self):
        pass

    def Connect(self):
        pass

    def CopyCrop(self):
        pass

    def CopyImage(self):
        pass

    def CreateChannels(self):
        pass

    def CropImage(self):
        pass

    def DeleteChannels(self):
        pass

    def Disconnect(self):
        pass

    def Fill(self):
        pass

    def Get16Gray(self):
        pass

    def Get16GrayFloat(self):
        pass

    def GetAspect(self):
        pass

    def GetBitmapInfo(self):
        pass

    def GetFiltered(self):
        pass

    def GetFilteredHDR(self):
        pass

    def GetFlags(self):
        pass

    def GetGamma(self):
        pass

    def GetHDRPixel(self):
        pass

    def GetHeight(self):
        pass

    def GetLinearHDRPixel(self):
        pass

    def GetLinearPixel(self):
        pass

    def GetMaxAlphaLevel(self):
        pass

    def GetMaxRGBLevel(self):
        pass

    def GetOpenMode(self):
        pass

    def GetPixel(self):
        pass

    def GetType(self):
        pass

    def GetUseScaleColors(self):
        pass

    def GetWidth(self):
        pass

    def HasAlpha(self):
        pass

    def HasGamma(self):
        pass

    def HasPreMultipliedAlpha(self):
        pass

    def IsDithered(self):
        pass

    def IsHighDynamicRange(self):
        pass

    def IsPaletted(self):
        pass

    def MapReady(self):
        pass

    def Put16Gray(self):
        pass

    def Put16GrayFloat(self):
        pass

    def PutHDRPixel(self):
        pass

    def PutPixel(self):
        pass

    def ScaleColor(self):
        pass

    def ScaleColorA(self):
        pass

    def SetFlags(self):
        pass

    def SetGamma(self):
        pass

    def SetHasGamma(self):
        pass

    def SetUseScaleColors(self):
        pass


class FrameRendParams(BaseInterfaceServer):
    def GetAmbient(self):
        pass

    def GetBackground(self):
        pass

    def GetBlowupCenter(self):
        pass

    def GetBlowupFactor(self):
        pass

    def GetFrameDuration(self):
        pass

    def GetGlobalLightLevel(self):
        pass

    def GetRegxmax(self):
        pass

    def GetRegxmin(self):
        pass

    def GetRegymax(self):
        pass

    def GetRegymin(self):
        pass

    def GetRelSubFrameDuration(self):
        pass

    def SetAmbient(self):
        pass

    def SetBackground(self):
        pass

    def SetBlowupCenter(self):
        pass

    def SetBlowupFactor(self):
        pass

    def SetFrameDuration(self):
        pass

    def SetGlobalLightLevel(self):
        pass

    def SetRegxmax(self):
        pass

    def SetRegxmin(self):
        pass

    def SetRegymax(self):
        pass

    def SetRegymin(self):
        pass

    def SetRelSubFrameDuration(self):
        pass


class IObject(BaseInterfaceServer):
    def GetIObjectName(self):
        pass
    def Init(self):
        pass


class Mesh(BaseInterfaceServer):
    AffectRegionFunction = ()

    AlphaMap = ()

    ColorPerVertexMap = ()

    CombineMeshes = ()

    CustomMaps = ()

    DefaultMap = ()

    FaceCenters = ()

    FaceNormals = ()

    Faces = ()

    FaceVertices = ()

    GetDisplayBackFaceVertices = ()

    GetHandleBoxType = ()

    GetMapChannelID = ()

    GetMapChannelNum = ()

    GetUseVertexDots = ()

    GetUseVisEdge = ()

    GetVertexDotType = ()

    NumCustomMaps = ()

    NumFaces = ()

    NumVertices = ()

    SetDisplayBackFaceVertices = ()

    SetHandleBoxType = ()

    SetUseVertexDots = ()

    SetUseVisEdge = ()

    SetVertexDotType = ()

    ShadingMap = ()

    SliceMesh = ()

    SmoothFlags = ()

    thisown = ()

    VertexDataType = ()

    Vertices = ()

    def AffectRegionFunction(self):
        pass

    def AngleBetweenFaces(self):
        pass

    def ApplyUVWMap(self):
        pass

    def AutoSmooth(self):
        pass

    def AverageSelVertCenter(self):
        pass

    def AverageSelVertNormal(self):
        pass

    def BaryCoords(self):
        pass

    def BreakVerts(self):
        pass

    def BuildBoundingBox(self):
        pass

    def BuildNormals(self):
        pass

    def BuildVisEdgeList(self):
        pass

    def CheckNormals(self):
        pass

    def ClearDispFlag(self):
        pass

    def ClearFlag(self):
        pass

    def ClearSpecifiedNormals(self):
        pass

    def ClearVertexWeights(self):
        pass

    def ClearVSelectionWeights(self):
        pass

    def CloneFaces(self):
        pass

    def CombineMeshes(self):
        pass

    def CopyBasics(self):
        pass

    def DeepCopy(self):
        pass

    def DeleteFaceSet(self):
        pass

    def DeleteFlaggedFaces(self):
        pass

    def DeleteIsoVerts(self):
        pass

    def DeleteSelected(self):
        pass

    def DeleteVertSet(self):
        pass

    def DeselectHiddenEdges(self):
        pass

    def DeselectHiddenFaces(self):
        pass

    def DisplayAllEdges(self):
        pass

    def DisplayNormals(self):
        pass

    def DivideEdge(self):
        pass

    def DivideFace(self):
        pass

    def DoesFaceExist(self):
        pass

    def EdgeTessellate(self):
        pass

    def ElementFromFace(self):
        pass

    def EnableEdgeList(self):
        pass

    def ExtrudeFaces(self):
        pass

    def FaceCenter(self):
        pass

    def FaceCenterTessellate(self):
        pass

    def FaceNormal(self):
        pass

    def FaceSel(self):
        pass

    def FindOpenEdges(self):
        pass

    def FindVertsUsedOnlyByFaces(self):
        pass

    def FitMaterialToMeshIDs(self):
        pass

    def FitMeshIDsToMaterial(self):
        pass

    def FlipNormal(self):
        pass

    def FreeAll(self):
        pass

    def FreeChannels(self):
        pass

    def FreeVertexWeights(self):
        pass

    def FreeVSelectionWeights(self):
        pass

    def GetAlphaMap(self):
        pass

    def GetBoundingBox(self):
        pass

    def GetColorPerVertexMap(self):
        pass

    def GetCustomMap(self):
        pass

    def GetDefaultMap(self):
        pass

    def GetDispFlag(self):
        pass

    def GetDispFlags(self):
        pass

    def GetDisplayBackFaceVertices(self):
        pass

    def GetEdgeSel(self):
        pass

    def GetFace(self):
        pass

    def GetFaceCenter(self):
        pass

    def GetFaceMtlIndex(self):
        pass

    def GetFaceNormal(self):
        pass

    def GetFaceSel(self):
        pass

    def GetFaceVertex(self):
        pass

    def GetFaceVertices(self):
        pass

    def GetFlag(self):
        pass

    def GetHandleBoxType(self):
        pass

    def GetIsoMapVerts(self):
        pass

    def GetIsoVerts(self):
        pass

    def GetMapChannelID(self):
        pass

    def GetMapChannelNum(self):
        pass

    def GetMtlIndex(self):
        pass

    def GetNormalCount(self):
        pass

    def GetNormalsBuilt(self):
        pass

    def GetNumCustomMaps(self):
        pass

    def GetNumFaces(self):
        pass

    def GetNumTVerts(self):
        pass

    def GetNumVertices(self):
        pass

    def GetRenderedVertexNormal(self):
        pass

    def GetSelLevel(self):
        pass

    def GetShadingMap(self):
        pass

    def GetSmoothFlags(self):
        pass

    def GetTVert(self):
        pass

    def GetTVFace(self):
        pass

    def GetUseVertexDots(self):
        pass

    def GetUseVisEdge(self):
        pass

    def GetVertex(self):
        pass

    def GetVertexDotType(self):
        pass

    def GetVertexFlag(self):
        pass

    def GetVertexWeights(self):
        pass

    def GetVertHide(self):
        pass

    def GetVertSel(self):
        pass

    def GetVSelectionWeights(self):
        pass

    def HiddenFacesToVerts(self):
        pass

    def IndentSelFaces(self):
        pass

    def Init(self):
        pass

    def IntersectRay(self):
        pass

    def InvalidateEdgeList(self):
        pass

    def InvalidateGeomCache(self):
        pass

    def InvalidateTopologyCache(self):
        pass

    def InvalidateVertexCache(self):
        pass

    def IsFaceCacheInvalid(self):
        pass

    def MakeMapPlanar(self):
        pass

    def NewAndCopyChannels(self):
        pass

    def Optimize(self):
        pass

    def PolyFromFace(self):
        pass

    def ReduceDisplayCaches(self):
        pass

    def RemoveDegenerateFaces(self):
        pass

    def RemoveIllegalFaces(self):
        pass

    def SetDispFlag(self):
        pass

    def SetDisplayBackFaceVertices(self):
        pass

    def SetFaceMtlIndex(self):
        pass

    def SetFaceNormal(self):
        pass

    def SetFlag(self):
        pass

    def SetHandleBoxType(self):
        pass

    def SetNormal(self):
        pass

    def SetNumFaces(self):
        pass

    def SetNumVerts(self):
        pass

    def SetSmoothFlags(self):
        pass

    def SetStaticMesh(self):
        pass

    def SetTVert(self):
        pass

    def SetUseVertexDots(self):
        pass

    def SetUseVisEdge(self):
        pass

    def SetVert(self):
        pass

    def SetVertexDotType(self):
        pass

    def SetVertexFlag(self):
        pass

    def ShallowCopy(self):
        pass

    def SliceMesh(self):
        pass

    def SupportVertexWeights(self):
        pass

    def SupportVSelectionWeights(self):
        pass

    def TurnEdge(self):
        pass

    def UnifyNormals(self):
        pass

    def VertexDataType(self):
        pass

    def VertexTempSel(self):
        pass

    def VertSel(self):
        pass

    def WeldCollinear(self):
        pass

    def ZeroTopologyCache(self):
        pass


class ModContext(BaseInterfaceServer):
    def GetBox(self):
        pass
    def GetTM(self):
        pass


class ParamBlockDesc2(BaseInterfaceServer):
    def AddInterface(self):
        pass

    def Count(self):
        pass

    def GetAColor(self):
        pass

    def GetBitmap(self):
        pass

    def GetColor(self):
        pass

    def GetFloat(self):
        pass

    def GetInitFile(self):
        pass

    def GetINode(self):
        pass

    def GetInt(self):
        pass

    def GetMtl(self):
        pass

    def GetOwnerRefNo(self):
        pass

    def GetPoint3(self):
        pass

    def GetPoint4(self):
        pass

    def GetReferenceTarget(self):
        pass

    def GetStr(self):
        pass

    def GetString(self):
        pass

    def GetSubMtlNo(self):
        pass

    def GetSubTexNo(self):
        pass

    def GetTexmap(self):
        pass

    def GetTimeValue(self):
        pass

    def IDtoIndex(self):
        pass

    def IndextoID(self):
        pass

    def InvalidateUI(self):
        pass

    def NameToIndex(self):
        pass

    def RemoveInterface(self):
        pass

    def SetFileTypes(self):
        pass

    def SetInitFile(self):
        pass

    def SetOwnerRefNo(self):
        pass

    def SetSubMtlNo(self):
        pass

    def SetSubTexNo(self):
        pass

    def Version(self):
        pass


class ViewParams(BaseInterfaceServer):
    def GetAffineTM(self):
        pass

    def GetDistance(self):
        pass

    def GetFarRange(self):
        pass

    def GetFov(self):
        pass

    def GetHither(self):
        pass

    def GetNearRange(self):
        pass

    def GetPrevAffineTM(self):
        pass

    def GetProjType(self):
        pass

    def GetYon(self):
        pass

    def GetZoom(self):
        pass

    def SetAffineTM(self):
        pass

    def SetDistance(self):
        pass

    def SetFarRange(self):
        pass

    def SetFov(self):
        pass

    def SetHither(self):
        pass

    def SetNearRange(self):
        pass

    def SetPrevAffineTM(self):
        pass

    def SetProjType(self):
        pass

    def SetYon(self):
        pass

    def SetZoom(self):
        pass


class CUIFrame(ICustomControl):
    ContentHandle = ()

    ContentType = ()

    Create = ()

    Hidden = ()

    Name = ()

    Position = ()

    PosType = ()

    thisown = ()

    def Create(self):
        pass

    def Dock(self):
        pass

    def Float(self):
        pass

    def GetContentHandle(self):
        pass

    def GetContentType(self):
        pass

    def GetName(self):
        pass

    def GetPosition(self):
        pass

    def GetPosType(self):
        pass

    def Hide(self):
        pass

    def IsFloating(self):
        pass

    def IsHidden(self):
        pass

    def Minimize(self):
        pass

    def SetContentHandle(self):
        pass

    def SetContentType(self):
        pass

    def SetName(self):
        pass

    def SetPosition(self):
        pass

    def SetPosType(self):
        pass


class ReferenceTarget(ReferenceMaker):
    thisown = ()
    def NotifyTarget(self):
        pass


class Control(ReferenceTarget):
    thisown = ()
    def AppendEaseCurve(self):
        pass

    def AppendMultCurve(self):
        pass

    def ApplyEase(self):
        pass

    def CanApplyEaseMultCurves(self):
        pass

    def CanInstanceController(self):
        pass

    def ChangeParents(self):
        pass

    def ClearSelection(self):
        pass

    def CommitValue(self):
        pass

    def Copy(self):
        pass

    def CreateLockKey(self):
        pass

    def DeleteEaseCurve(self):
        pass

    def DeleteMultCurve(self):
        pass

    def EnableORTs(self):
        pass

    def GetDOFParams(self):
        pass

    def GetFloatValue(self):
        pass

    def GetInheritanceFlags(self):
        pass

    def GetInheritsParentTransform(self):
        pass

    def GetMatrixValue(self):
        pass

    def GetMultVal(self):
        pass

    def GetNumEaseCurves(self):
        pass

    def GetNumMultCurves(self):
        pass

    def GetORT(self):
        pass

    def GetPoint2Value(self):
        pass

    def GetPoint3Value(self):
        pass

    def GetPoint4Value(self):
        pass

    def GetPositionController(self):
        pass

    def GetQuatValue(self):
        pass

    def GetRollController(self):
        pass

    def GetRotationController(self):
        pass

    def GetScaleController(self):
        pass

    def GetScaleValue(self):
        pass

    def GetTarget(self):
        pass

    def GetWController(self):
        pass

    def GetXController(self):
        pass

    def GetYController(self):
        pass

    def GetZController(self):
        pass

    def InvertSelection(self):
        pass

    def IsColorController(self):
        pass

    def IsFloatController(self):
        pass

    def IsKeyable(self):
        pass

    def IsLeaf(self):
        pass

    def IsMatrixController(self):
        pass

    def IsPoint2Controller(self):
        pass

    def IsPoint3Controller(self):
        pass

    def IsPoint4Controller(self):
        pass

    def IsQuatController(self):
        pass

    def IsReplaceable(self):
        pass

    def IsScaleController(self):
        pass

    def IsVisibleInViewports(self):
        pass

    def OKToBindToNode(self):
        pass

    def RescaleTime(self):
        pass

    def RestoreValue(self):
        pass

    def SelectAll(self):
        pass

    def SetFloatValue(self):
        pass

    def SetInheritanceFlags(self):
        pass

    def SetMatrixValue(self):
        pass

    def SetMatrixValuePosition(self):
        pass

    def SetMatrixValueRotate(self):
        pass

    def SetMatrixValueScale(self):
        pass

    def SetORT(self):
        pass

    def SetPoint2Value(self):
        pass

    def SetPoint3Value(self):
        pass

    def SetPoint4Value(self):
        pass

    def SetPositionController(self):
        pass

    def SetQuatValue(self):
        pass

    def SetRollController(self):
        pass

    def SetRotationController(self):
        pass

    def SetScaleController(self):
        pass

    def SetScaleValue(self):
        pass

    def SetTarget(self):
        pass

    def SubMove(self):
        pass

    def SubRotate(self):
        pass

    def SubScale(self):
        pass


class CustomAttribute(ReferenceTarget):
    thisown = ()
    def GetName(self):
        pass


class IMultiPassCameraEffect(ReferenceTarget):
    thisown = ()


class INode(ReferenceTarget):
    AllEdges = ()
    ApplyAtmospherics = ()
    AttachNodesToGroup = ()
    BackfaceCull = ()
    BaseObject = ()
    BoxMode = ()
    CastShadows = ()
    Children = ()
    CloseGroup = ()
    DeleteNodes = ()
    DetachNodesFromGroup = ()
    ExplodeNodes = ()
    FaceCount = ()
    FindNodeFromBaseObject = ()
    FlashNodes = ()
    Freeze = ()
    GBufferID = ()
    GetAffectChildren = ()
    GetINodeByHandle = ()
    GetINodeByName = ()
    GetINodeFromRenderID = ()
    GetPivotMode = ()
    GroupNodes = ()
    Hide = ()
    IgnoreExtents = ()
    InheritVisibility = ()
    IsRoot = ()
    LayerName = ()
    LocalPosition = ()
    LocalRotation = ()
    LocalScaling = ()
    LocalTransform = ()
    Material = ()
    Modifiers = ()
    MotionBlurEnabled = ()
    MotionBlurMultiplier = ()
    MotionBlurType = ()
    Name = ()
    NeverDegrade = ()
    NodeColorPicker = ()
    NumChildren = ()
    NumModifiers = ()
    Object = ()
    OpenGroup = ()
    Parent = ()
    Position = ()
    PrimaryVisibility = ()
    ReceiveShadows = ()
    Renderable = ()
    RenderOccluded = ()
    Rotation = ()
    Scaling = ()
    SecondaryVisibility = ()
    SeeThrough = ()
    SetAffectChildren = ()
    SetNodeAttribute = ()
    SetPivotMode = ()
    ShadeVertexColors = ()
    ShowFrozenWithMtl = ()
    thisown = ()
    Trajectory = ()
    Transform = ()
    UngroupNodes = ()
    VertexColorMapChannel = ()
    VertexColorMode = ()
    VertexColorType = ()
    VertexCount = ()
    VertexTicks = ()
    Visibility = ()
    WireColor = ()
    X = ()
    Y = ()
    Z = ()

    def AddModifier(self, Modifier):
        pass

    def AddNewXRefFile(self, Asset):
        pass

    def AlignPivot(self, TimeValue, bool):
        pass

    def AlignToParent(self, TimeValue):
        pass

    def AlignToWorld(self, TimeValue):
        pass

    def AttachChild(self, INode):
        pass

    def AttachNodesToGroup(self, INodeTab, INode):
        pass

    def BindToTarget(self, INode):
        pass

    def BindXRefFile(self, int):
        pass

    def BoneAsLine(self, bool):
        pass

    def CenterPivot(self, TimeValue, bool):
        pass

    def CloseGroup(self, INodeTab):
        pass

    def Collapse(self):
        pass

    def CollapseTo(self, modIndex):
        pass

    def Convert(self, Class_ID):
        pass

    def CopyProperties(self, INode):
        pass

    def CreateCopy(self):
        return INode()

    def CreateInstance(self):
        return INode()

    def CreateReference(self):
        return INode()

    def CreateTreeCopy(self):
        return INode()

    def CreateTreeInstance(self):
        return INode()

    def CreateTreeReference(self):
        return INode()

    def Delete(self, TimeValue):
        pass

    def DeleteAllXRefs(self):
        pass

    def DeleteModifier(self, int):
        pass

    def DeleteNodes(self, isKeepChildTM, isRedraw, isOverrideSlaveTM):
        pass

    def DeleteXRefFile(self, int):
        pass

    def Deselect(self):
        pass

    def Detach(self, TimeValue):
        pass

    def DetachNodesFromGroup(self, INodeTab):
        pass

    def DisposeTemporary(self):
        pass

    def EvalWorldState(self, TimeValue):
        return ObjectState()

    def ExplodeNodes(self, INodeTab):
        pass

    def FindNodeFromBaseObject(self):
        return INode()

    def FlagForeground(self, TimeValue):
        pass

    def FlagXrefChanged(self, int):
        pass

    def FlashNodes(self, INodeTab):
        pass

    def Freeze(self, bool):
        pass

    def GetActualINode(self):
        return INode()

    def GetAffectChildren(self):
        return True

    def GetAllEdges(self):
        return True

    def GetApplyAtmospherics(self):
        return True

    def GetAssemblyBBoxDisplay(self):
        return True

    def GetBackCull(self):
        return True

    def GetBaseObject(self):
        return Object()

    def GetBoneAutoAlign(self):
        return True

    def GetBoneAxis(self):
        return 0

    def GetBoneAxisFlip(self):
        return True

    def GetBoneFreezeLen(self):
        return True

    def GetBoneNodeOnOff(self):
        return True

    def GetBoneNodeOnOff_T(self, TimeValue):
        return True

    def GetBoneScaleType(self):
        return 0

    def GetBoxMode(self):
        return True

    def GetCastShadows(self):
        return True

    def GetChild(self, int):
        return INode()

    def GetDerivedObject(self):
        return IDerivedObject()

    def GetDesc(self):
        return FPInterface()

    def GetDisplayByLayer(self):
        return True

    def GetFaceCount(self, TimeValue):
        return 0

    def GetGBufID(self):
        return ULONG()

    def GetGenerateCaustics(self):
        return True

    def GetGenerateGlobalIllum(self):
        return True

    def GetHandle(self):
        return ULONG()

    def GetIgnoreExtents(self):
        return True

    def GetImageBlurMultiplier(self, TimeValue):
        return 0.0

    def GetInheritVisibility(self):
        return True

    def GetINodeByHandle(self, ULONG):
        return INode()

    def GetINodeByName(self, name):
        return INode()

    def GetINodeFromRenderID(self, DWORD):
        return INode()

    def GetIsRoot(self):
        return True

    def GetLayer(self):
        return Layer()

    def GetLayerName(self):
        return ''

    def GetLocalPosition(self, TimeValue):
        return Point3()

    def GetLocalRotation(self, TimeValue):
        return Quat()

    def GetLocalScale(self, TimeValue):
        return Point3()

    def GetLocalTM(self, TimeValue):
        return Matrix3()

    def GetLookatNode(self):
        return INode()

    def GetMaterial(self):
        return Mtl()

    def GetModifier(self):
        return Modifier()

    def GetMotionBlurOnOff(self):
        return True

    def GetMotionBlurType(self):
        return 0

    def GetMotionByLayer(self):
        return True

    def GetName(self):
        return ''

    def GetNeverDegrade(self):
        return True

    def GetNumChildren(self):
        return 0

    def GetNumModifiers(self):
        return 0

    def GetObject(self):
        return Object()

    def GetObjectRef(self):
        return Object()

    def GetObjectTM(self, TimeValue):
        return Matrix3()

    def GetObjOffsetPosition(self):
        return Point3()

    def GetObjOffsetRotation(self):
        return Quat()

    def GetObjOffsetScale(self):
        return ScaleValue()

    def GetObjOrWSMRef(self):
        return Object()

    def GetObjTMAfterWSM(self, TimeValue):
        return Matrix3()

    def GetObjTMBeforeWSM(self, TimeValue):
        return Matrix3()

    def GetParent(self):
        return INode()

    def GetParentTM(self, TimeValue):
        return Matrix3()

    def GetPivotMode(self):
        return 0

    def GetPositionTaskWeight(self):
        return 0.0

    def GetPositionX(self, TimeValue):
        return 0.0

    def GetPositionY(self, TimeValue):
        return 0.0

    def GetPositionZ(self, TimeValue):
        return 0.0

    def GetPrimaryVisibility(self):
        return True

    def GetReceiveCaustics(self):
        return True

    def GetReceiveGlobalIllum(self):
        return True

    def GetReceiveShadows(self):
        return True

    def GetRenderable(self):
        return True

    def GetRenderByLayer(self):
        return True

    def GetRenderOccluded(self):
        return True

    def GetRotationTaskWeight(self):
        return 0.0

    def GetSecondaryVisibility(self):
        return True

    def GetSeeThrough(self):
        return True

    def GetSeeThroughObject(self):
        return True

    def GetSelected(self):
        return True

    def GetShadeVertexColors(self):
        return True

    def GetShowFrozenWithMtl(self):
        return True

    def GetStretchTM(self):
        return Matrix3()

    def GetTarget(self):
        return INode()

    def GetTargetNodePair(self):
        return True

    def GetTargetTM(self, Matrix3):
        return True

    def GetTaskAxisState(self, which, axis):
        return True

    def GetTaskAxisStateBits(self):
        return DWORD()

    def GetTMController(self):
        return Control()

    def GetTrajectoryON(self):
        return True

    def GetTransformLock(self, type, axis):
        return True

    def GetUserPropBuffer(self, WStr):
        pass

    def GetVertexColorMapChannel(self):
        return 0

    def GetVertexColorMode(self):
        return True

    def GetVertexColorType(self):
        return 0

    def GetVertexCount(self, TimeValue):
        return 0

    def GetVertTicks(self):
        return True

    def GetVisibility(self, TimeValue):
        return True

    def GetVisibilityController(self):
        return Control()

    def GetWireColor(self):
        return Color()

    def GetWorldPosition(self, TimeValue):
        return Point3()

    def GetWorldRotation(self, TimeValue):
        return Quat()

    def GetWorldScale(self, TimeValue):
        return Point3()

    def GetWorldTM(self, TimeValue):
        return Matrix3()

    def GetXRefFile(self, int):
        return Asset()

    def GetXRefFileCount(self):
        return 0

    def GetXRefFlags(self, int):
        return DWORD()

    def GetXRefParent(self, int):
        return INode()

    def GetXRefTree(self, int):
        return INode()

    def GroupNodes(self, WStr, bool):
        return INode()

    def Hide(self, bool):
        pass

    def InsertModifier(self, Modifier, int):
        pass

    def InvalidateObjectCache(self):
        pass

    def InvalidateRect(self, TimeValue):
        pass

    def InvalidateTM(self):
        pass

    def InvalidateTreeTM(self):
        pass

    def InvalidateWS(self):
        pass

    def IsActiveGrid(self):
        return True

    def IsAssemblyHead(self):
        return True

    def IsAssemblyHeadMemberOf(self, INode):
        return True

    def IsAssemblyHeadOpen(self):
        return True

    def IsAssemblyMember(self):
        return True

    def IsAssemblyMemberOpen(self):
        return True

    def IsBoneOnly(self):
        return True

    def IsBoneShowing(self):
        return True

    def IsDependent(self):
        return True

    def IsFrozen(self):
        return True

    def IsGroupHead(self):
        return True

    def IsGroupMember(self):
        return True

    def IsHidden(self):
        return True

    def IsNodeHidden(self):
        return True

    def IsObjectFrozen(self):
        return True

    def IsObjectHidden(self):
        return True

    def IsOpenGroupHead(self):
        return True

    def IsOpenGroupMember(self):
        return True

    def IsSceneXRef(self):
        return True

    def IsTarget(self):
        return True

    def MayResetTransform(self):
        return True

    def Move(self, Point3, TimeValue):
        pass

    def NodeColorPicker(self, DWORD):
        return True

    def OpenGroup(self, INodeTab, bool):
        pass

    def RealignBoneToChild(self, TimeValue):
        pass

    def ReloadXRef(self,int):
        return True

    def ResetBoneStretch(self, TimeValue):
        pass

    def ResetPivot(self, TimeValue):
        pass

    def ResetTransform(self, TimeValue, isScaleOnly):
        pass

    def Rotate(self, Quat, TimeValue):
        pass

    def Scale(self, Point3, TimeValue):
        pass

    def Select(self):
        pass

    def SetAffectChildren(self, bool):
        pass

    def SetAllEdges(self, onOff):
        pass

    def SetApplyAtmospherics(self, onOff):
        pass

    def SetAssemblyBBoxDisplay(self, bool):
        pass

    def SetAssemblyHead(self, bool):
        pass

    def SetAssemblyHeadOpen(self, bool):
        pass

    def SetAssemblyMember(self, bool):
        pass

    def SetAssemblyMemberOpen(self, bool):
        pass

    def SetBackCull(self, bool):
        pass

    def SetBaseObject(self, Object):
        pass

    def SetBoneAutoAlign(self, bool):
        pass

    def SetBoneAxis(self, int):
        pass

    def SetBoneAxisFlip(self, bool):
        pass

    def SetBoneFreezeLen(self, bool):
        pass

    def SetBoneNodeOnOff(self, bool):
        pass

    def SetBoneScaleType(self, int):
        pass

    def SetBoxMode(self, bool):
        pass

    def SetCastShadows(self, bool):
        pass

    def SetDisplayByLayer(self, bool):
        pass

    def SetGBufID(self, ULONG):
        pass

    def SetGenerateCaustics(self, bool):
        pass

    def SetGenerateGlobalIllum(self, bool):
        pass

    def SetGroupHead(self, bool):
        pass

    def SetGroupHeadOpen(self, bool):
        pass

    def SetGroupMember(self, bool):
        pass

    def SetGroupMemberOpen(self, bool):
        pass

    def SetIgnoreExtents(self, bool):
        pass

    def SetImageBlurMultiplier(self, float, TimeValue):
        pass

    def SetInheritVisibility(self, bool):
        pass

    def SetIsTarget(self, bool):
        pass

    def SetLocalPosition(self, Point3, TimeValue):
        pass

    def SetLocalRotation(self, Quat, TimeValue):
        pass

    def SetLocalScale(self, Point3, TimeValue):
        pass

    def SetLocalTM(self, Matrix3, TimeValue):
        pass

    def SetMaterial(self, Mtl):
        pass

    def SetMotionBlurOnOff(self, bool):
        pass

    def SetMotionBlurType(self, int):
        pass

    def SetMotionByLayer(self, bool):
        pass

    def SetName(self, name):
        pass

    def SetNeverDegrade(self, bool):
        pass

    def SetNodeAttribute(self, INodeTab, int, bool):
        pass

    def SetNodeTMRelConstPlane(self, Matrix3):
        pass

    def SetObject(self, Object):
        pass

    def SetObjectRef(self, Object):
        pass

    def SetObjOffsetPosition(self, Point3):
        pass

    def SetObjOffsetRotation(self, Quat):
        pass

    def SetObjOffsetScale(self, Point3):
        pass

    def SetParent(self, INode):
        pass

    def SetPivotMode(self, int):
        pass

    def SetPositionTaskWeight(self, float):
        pass

    def SetPositionX(self, float):
        pass

    def SetPositionY(self, float):
        pass

    def SetPositionZ(self, float):
        pass

    def SetPrimaryVisibility(self, bool):
        pass

    def SetReceiveCaustics(self, bool):
        pass

    def SetReceiveGlobalIllum(self, bool):
        pass

    def SetReceiveShadows(self, bool):
        pass

    def SetRenderable(self, bool):
        pass

    def SetRenderByLayer(self, bool):
        pass

    def SetRenderOccluded(self, bool):
        pass

    def SetRotationTaskWeight(self, float):
        pass

    def SetSecondaryVisibility(self, bool):
        pass

    def SetSeeThrough(self, bool):
        pass

    def SetShadeVertexColors(self, bool):
        pass

    def SetShowFrozenWithMtl(self, bool):
        pass

    def SetTargetNodePair(self, bool):
        pass

    def SetTaskAxisState(self, which, axis, isOnOff):
        pass

    def SetTMController(self, Control):
        return True

    def SetTrajectoryON(self, bool):
        pass

    def SetTransformLock(self, type, axis, isOnOff):
        pass

    def SetUserPropBuffer(self, WStr):
        pass

    def SetVertexColorMapChannel(self, int):
        pass

    def SetVertexColorMode(self, bool):
        pass

    def SetVertexColorType(self, int):
        pass

    def SetVertTicks(self, bool):
        pass

    def SetVisibility(self, float, TimeValue):
        pass

    def SetVisibilityController(self, Control):
        pass

    def SetWireColor(self, Color):
        pass

    def SetWorldPosition(self, Point3, TimeValue):
        pass

    def SetWorldRotation(self, Quat, TimeValue):
        pass

    def SetWorldScale(self, Point3, TimeValue):
        pass

    def SetWorldTM(self, Matrix3, TimeValue):
        pass

    def SetXRefFile(self, int, Asset, isReload):
        pass

    def SetXRefFlags(self, int, DWORD, isOnOff):
        pass

    def SetXRefParent(self, int, INode):
        pass

    def ShowBone(self, bool):
        pass

    def UnfreezeObjectAndLayer(self):
        pass

    def UngroupNodes(self, INodeTab):
        pass

    def UnhideObjectAndLayer(self):
        pass

    def UpdateChangedXRefs(self):
        pass

    def WorldAlignPivot(self, TimeValue, isMoveObject):
        pass


class IParamBlock(ReferenceTarget):
    thisown = ()
    def AnimNumToParamNum(self, animNum):
        return 0

    def GetAnimNum(self, parentNum):
        return 0

    def GetAnimParamControlType(self, int):
        return SClass_ID()

    def GetColor(self, int, TimeValue):
        return Color()

    def GetController(self, int):
        return Control()

    def GetFloat(self, int, TimeValue):
        return 0.0

    def GetInt(self, int, TimeValue):
        return 0

    def GetParamBlock(self):
        return IParamBlock()

    def GetParameterType(self, int):
        return 0

    def GetPoint3(self, int, TimeValue):
        return Point3()

    def GetRefNum(self, parentNum):
        return 0

    def GetValue(self, int, TimeValue, float, Interval):
        return True

    def GetVersion(self):
        return DWORD()

    def LastNotifyParamNum(self):
        return 0

    def NumParams(self):
        return 0

    def RemoveController(self, int):
        pass

    def RescaleParam(self, int, float):
        pass

    def SetController(self, int, Control):
        pass

    def SetValue(self, int, TimeValue, value):
        pass

    def SwapControllers(self, int1, int2):
        pass


class IParamBlock2(ReferenceTarget):
    thisown = ()
    def AnimNumToParamNum(self, animNum, tabIndex):
        return 0

    def Append(self, ParamID, value):
        return 0

    def Assign(self, id, IParamBlock2, src_id):
        pass

    def ClearSubAnimMap(self):
        pass

    def Count(self, ParamID):
        return 0

    def Delete(self, ParamID, start, num):
        return 0

    def FindRefParam(self, ReferenceTarget, tabIndex):
        return ParamID()

    def GetAColor(self, ParamID, TimeValue, tabIndex):
        return AColor()

    def GetAnimNum(self, ParamID, tabIndex):
        return 0

    def GetAnimParamControlType(self, int):
        return SClass_ID()

    def GetAsset(self, ParamID, TimeValue):
        return Asset()

    def GetBitmap(self, ParamID, TimeValue):
        return PBBitmap()

    def GetColor(self, ParamID, TimeValue):
        return Color()

    def GetControllerByID(self, ParamID):
        return Control()

    def GetControllerByIndex(self, int):
        return Control()

    def GetControllerRefNum(self, int):
        return 0

    def GetDesc(self):
        return ParamBlockDesc2()

    def GetFloat(self, ParamID, TimeValue):
        return 0.0

    def GetINode(self, ParamID, TimeValue):
        return INode()

    def GetInt(self, ParamID, TimeValue):
        return 0

    def GetLocalName(self):
        return ''

    def GetMatrix3(self, ParamID, TimeValue):
        return Matrix3()

    def GetMtl(self, ParamID, TimeValue):
        return Mtl()

    def GetOwner(self):
        return ReferenceMaker()

    def GetParamBlock2(self, ParamID, TimeValue):
        return IParamBlock2()

    def GetParamControlType(self, ParamID):
        return SClass_ID()

    def GetParamDimension(self, int):
        return ParamDimension()

    def GetParameterType(self, ParamID):
        return ParamType2()

    def GetPoint3(self, ParamID, TimeValue):
        return Point3()

    def GetPoint4(self, ParamID, TimeValue):
        return Point4()

    def GetReferenceTarget(self, ParamID, TimeValue):
        return ReferenceTarget()

    def GetRefNum(self, int):
        return 0

    def GetStr(self, ParamID, TimeValue):
        return ''

    def GetTexmap(self, ParamID, TimeValue):
        return Texmap()

    def GetTimeValue(self, ParamID, TimeValue):
        return TimeValue()

    def GetVersion(self):
        return DWORD()

    def ID(self):
        return 0

    def IDtoIndex(self, ParamID):
        return 0

    def IndextoID(self, int):
        return ParamID()

    def Insert(self, ParamID, int, values):
        return 0

    def KeyFrameAtTimeByID(self, ParamID, TimeValue):
        return True

    def KeyFrameAtTimeByIndex(self, int, TimeValue):
        return True

    def NumParams(self):
        return 0

    def ReleaseDesc(self):
        pass

    def RemoveControllerByIndex(self, int, tabIndex):
        pass

    def RescaleParam(self, paramNum, tabIndex, float):
        pass

    def Reset(self, ParamID, tabIndex):
        pass

    def ResetAll(self):
        pass

    def Resize(self, ParamID, num):
        return 0

    def SetControllerByID(self, ParamID, tabIndex, Control):
        pass

    def SetControllerByIndex(self, int, tabIndex, Control):
        pass

    def SetCount(self, ParamID, int):
        pass

    def SetDesc(self, ParamBlockDesc2):
        pass

    def SetSubAnimNum(self, ParamID, subAnimNum, tabIndex):
        pass

    def SetValue(self, ParamID, TimeValue, values):
        return True

    def Shrink(self, ParamID):
        pass

    def SwapControllers(self, int1, tabIndex1, int2, tabIndex2):
        pass

    def ZeroCount(self, ParamID):
        pass


class Layer(ReferenceTarget):
    thisown = ()
    def AddToLayer(self):
        pass

    def AllEdges(self):
        pass

    def ApplyAtmospherics(self):
        pass

    def BackCull(self):
        pass

    def BoxMode(self):
        pass

    def CastShadows(self):
        pass

    def DeleteFromLayer(self):
        pass

    def Freeze(self):
        pass

    def GetAllEdges(self):
        pass

    def GetBackCull(self):
        pass

    def GetBoxMode(self):
        pass

    def GetCVertMode(self):
        pass

    def GetDisplayFlags(self):
        pass

    def GetFlag(self):
        pass

    def GetFlag2(self):
        pass

    def GetIgnoreExtents(self):
        pass

    def GetImageBlurMultiplier(self):
        pass

    def GetInheritVisibility(self):
        pass

    def GetLocalVisibility(self):
        pass

    def GetMotionBlurOnOff(self):
        pass

    def GetName(self):
        pass

    def GetNodes(self):
        pass

    def GetPrimaryVisibility(self):
        pass

    def GetRenderFlags(self):
        pass

    def GetRenderOccluded(self):
        pass

    def GetSecondaryVisibility(self):
        pass

    def GetShadeCVerts(self):
        pass

    def GetTrajectory(self):
        pass

    def GetVertTicks(self):
        pass

    def GetVisibility(self):
        pass

    def GetWireColor(self):
        pass

    def HasObjects(self):
        pass

    def HasXRayMtl(self):
        pass

    def Hide(self):
        pass

    def IgnoreExtents(self):
        pass

    def IsFrozen(self):
        pass

    def IsHidden(self):
        pass

    def IsHiddenByVisControl(self):
        pass

    def MotionBlur(self):
        pass

    def RcvShadows(self):
        pass

    def Renderable(self):
        pass

    def SelectObjects(self):
        pass

    def SetApplyAtmospherics(self):
        pass

    def SetCastShadows(self):
        pass

    def SetCVertMode(self):
        pass

    def SetImageBlurMultiplier(self):
        pass

    def SetInheritVisibility(self):
        pass

    def SetMotionBlur(self):
        pass

    def SetMotionBlurOnOff(self):
        pass

    def SetName(self):
        pass

    def SetPrimaryVisibility(self):
        pass

    def SetRcvShadows(self):
        pass

    def SetRenderable(self):
        pass

    def SetRenderFlags(self):
        pass

    def SetRenderOccluded(self):
        pass

    def SetSecondaryVisibility(self):
        pass

    def SetShadeCVerts(self):
        pass

    def SetShowFrozenWithMtl(self):
        pass

    def SetVisibility(self):
        pass

    def SetWireColor(self):
        pass

    def ShowFrozenWithMtl(self):
        pass

    def Trajectory(self):
        pass

    def UpdateSelectionSet(self):
        pass

    def Used(self):
        pass

    def VertTicks(self):
        pass

    def XRayMtl(self):
        pass


class MaterialLibrary(ReferenceTarget):
    FileOpenMatLib = ()

    FileSaveAsMatLib = ()

    FileSaveMatLib = ()

    GetCurrentLibrary = ()

    GetNumSceneMaterials = ()

    GetSceneMaterial = ()

    GetSceneMaterialLibrary = ()

    LoadDefaultMaterialLibrary = ()

    Materials = ()

    NumMaterials = ()

    SceneMaterials = ()

    def Add(self):
        pass

    def DeleteAll(self):
        pass

    def FileOpenMatLib(self):
        pass

    def FileSaveAsMatLib(self):
        pass

    def FileSaveMatLib(self):
        pass

    def FindMaterial(self):
        pass

    def FindMaterialByName(self):
        pass

    def GetCurrentLibrary(self):
        pass

    def GetMaterial(self):
        pass

    def GetNumMaterials(self):
        pass

    def GetNumSceneMaterials(self):
        pass

    def GetSceneMaterial(self):
        pass

    def GetSceneMaterialLibrary(self):
        pass

    def LoadDefaultMaterialLibrary(self):
        pass

    def Remove(self):
        pass


class MtlBase(ReferenceTarget):
    thisown = ()
    def ActivateTexDisplay(self):
        pass

    def AnyMulti(self):
        pass

    def ClearMtlFlag(self):
        pass

    def DeactivateMapsInTree(self):
        pass

    def GetActiveMB(self):
        pass

    def GetFullName(self):
        pass

    def GetGBufID(self):
        pass

    def GetMeditObjType(self):
        pass

    def GetMEditRotate(self):
        pass

    def GetMeditTiling(self):
        pass

    def GetName(self):
        pass

    def GetRefTarget(self):
        pass

    def GetTransparencyHint(self):
        pass

    def IsMultiMtl(self):
        pass

    def LocalMappingsRequired(self):
        pass

    def LocalRequirements(self):
        pass

    def MappingsRequired(self):
        pass

    def MapSlotType(self):
        pass

    def Requirements(self):
        pass

    def Reset(self):
        pass

    def SetActiveMB(self):
        pass

    def SetGBufID(self):
        pass

    def SetMeditObjType(self):
        pass

    def SetMeditTiling(self):
        pass

    def SetMtlFlag(self):
        pass

    def SetName(self):
        pass

    def SupportsMultiMapsInViewport(self):
        pass

    def SupportTexDisplay(self):
        pass

    def TestMtlFlag(self):
        pass

    def TextureDisplayEnabled(self):
        pass

    def Update(self):
        pass

    def Validity(self):
        pass


class Renderer(ReferenceTarget):
    thisown = ()
    def ApplyRenderEffects(self, bitmap, timevalue, bool):
        return True

    def DoesSupportCustomRenderPresets(self):
        return True

    def DoesSupportTexureBaking(self):
        return True

    def GetAAFilterSupport(self):
        return 0

    def GetRenderPresetsFileVersion(self):
        return 0

    def GetRenderPresetsIsCompatible(self):
        return True

    def RenderPresetsMapCategoryToIndex(self):
        return 0

    def RenderPresetsMapIndexToCategory(self):
        return ''

    def ResetParams(self):
        pass


class SoundObj(ReferenceTarget):
    thisown = ()
    def GetTime(self):
        return TimeValue()

    def IsMute(self):
        return True

    def Play(self):
        return True

    def Playing(self):
        return True

    def Scrub(self):
        pass

    def SetMute(self):
        pass

    def Stop(self):
        return TimeValue()


class SpecialFX(ReferenceTarget):
    thisown = ()
    def Active(self):
        pass

    def AppendGizmo(self):
        pass

    def DeleteGizmo(self):
        pass

    def EditGizmo(self):
        pass

    def GetGizmo(self):
        pass

    def GetName(self):
        pass

    def GetNumGizmos(self):
        pass

    def GetSpecialFXName(self):
        pass

    def InsertGizmo(self):
        pass

    def OKGizmo(self):
        pass

    def SetSpecialFXName(self):
        pass

    def Update(self):
        pass


class BaseObject(ReferenceTarget):
    thisown = ()
    def ActivateSubSelSet(self):
        pass

    def ChangeTopology(self):
        pass

    def ClearSelection(self):
        pass

    def ForceNotify(self):
        pass

    def GetLocalBoundBox(self):
        pass

    def GetNamedSelSetName(self):
        pass

    def GetNumNamedSelSets(self):
        pass

    def GetNumSubObjTypes(self):
        pass

    def GetObjectName(self):
        pass

    def GetSubObjectLevel(self):
        pass

    def GetSubObjType(self):
        pass

    def GetSubObjTypeName(self):
        pass

    def GetWorldBoundBox(self):
        pass

    def HasUVW(self):
        pass

    def HasViewDependentBoundingBox(self):
        pass

    def HitTest(self):
        pass

    def InvertSelection(self):
        pass

    def Move(self):
        pass

    def NewSetFromCurSel(self):
        pass

    def OKToChangeTopology(self):
        pass

    def RemoveSubSelSet(self):
        pass

    def Rotate(self):
        pass

    def Scale(self):
        pass

    def SelectAll(self):
        pass

    def SetGenUVW(self):
        pass

    def SetNamedSelSetName(self):
        pass

    def SetupNamedSelDropDown(self):
        pass

    def SupportsNamedSubSels(self):
        pass

    def TransformCancel(self):
        pass

    def TransformFinish(self):
        pass

    def TransformHoldingFinish(self):
        pass

    def TransformHoldingStart(self):
        pass

    def TransformStart(self):
        pass



class Modifier(BaseObject):
    thisown = ()
    def ChangesSelType(self):
        pass

    def CopyAdditionalChannels(self):
        pass

    def DependOnTopology(self):
        pass

    def DisableMod(self):
        pass

    def DisableModApps(self):
        pass

    def DisableModInRender(self):
        pass

    def DisableModInViews(self):
        pass

    def EnableMod(self):
        pass

    def EnableModApps(self):
        pass

    def EnableModInRender(self):
        pass

    def EnableModInViews(self):
        pass

    def ForceNotify(self):
        pass

    def GetChannelsChanged(self):
        return ChannelMask()

    def GetChannelsUsed(self):
        return ChannelMask()

    def GetIDerivedObject(self):
        return IDerivedObject()

    def GetLocalValidity(self):
        return Interval()

    def GetName(self):
        return Wstr()

    def InputType(self):
        return Class_ID()

    def IsEnabled(self):
        pass

    def IsEnabledInRender(self):
        pass

    def IsEnabledInViews(self):
        pass

    def ModifyObject(self):
        pass

    def NeedUseSubselButton(self):
        pass

    def NotifyInputChanged(self):
        pass

    def SetName(self):
        pass

    def TotalChannelsChanged(self):
        return ChannelMask()

    def TotalChannelsUsed(self):
        return ChannelMask()


class OSModifier(Modifier):
    thisown = ()


class WSModifier(Modifier):
    thisown = ()


class Object(BaseObject):
    thisown = ()
    def ApplyUVWMap(self):
        pass

    def AsTriObject(self):
        pass

    def BranchDeleted(self):
        pass

    def CanCacheObject(self):
        pass

    def CanConvertToType(self):
        pass

    def CheckObjectIntegrity(self):
        pass

    def CollapseObject(self):
        pass

    def ContainedShapeSelectionArray(self):
        pass

    def ConvertToDerivedObject(self):
        pass

    def ConvertToType(self):
        pass

    def CopyAdditionalChannels(self):
        pass

    def CopyChannelLocks(self):
        pass

    def DeleteAllAdditionalChannels(self):
        pass

    def DoOwnSelectHilite(self):
        pass

    def Eval(self):
        pass

    def FindBaseObject(self):
        pass

    def FreeChannels(self):
        pass

    def GetBranchINode(self):
        pass

    def GetChannelLocks(self):
        pass

    def GetChannelValidity(self):
        pass

    def GetContainedShape(self):
        pass

    def GetContainedShapeMatrix(self):
        pass

    def GetDeformBBox(self):
        pass

    def GetExtendedProperties(self):
        pass

    def GetNoEvalInterval(self):
        pass

    def GetNumContainedShapes(self):
        pass

    def GetNumFaces(self):
        pass

    def GetNumMapChannels(self):
        pass

    def GetNumMapsUsed(self):
        pass

    def GetNumPipeBranches(self):
        pass

    def GetNumPoints(self):
        pass

    def GetNumSurfaces(self):
        pass

    def GetNumVerts(self):
        pass

    def GetObjectValidity(self):
        pass

    def GetPipeBranch(self):
        pass

    def GetPoint(self):
        pass

    def GetSubselState(self):
        pass

    def GetSurfacePoint(self):
        pass

    def GetWeight(self):
        pass

    def GetWorldSpaceObjectNode(self):
        pass

    def HasUVW(self):
        pass

    def HasWeights(self):
        pass

    def InitNodeName(self):
        pass

    def IntersectRay(self):
        pass

    def InvalidateChannels(self):
        pass

    def IsBaseClassOwnedChannel(self):
        pass

    def IsDeformable(self):
        pass

    def IsManipulator(self):
        pass

    def IsMappable(self):
        pass

    def IsObjectLocked(self):
        pass

    def IsParamSurface(self):
        pass

    def IsParticleSystem(self):
        pass

    def IsPointSelected(self):
        pass

    def IsRenderable(self):
        pass

    def IsShapeObject(self):
        pass

    def IsWorldSpaceObject(self):
        pass

    def LockChannels(self):
        pass

    def LockObject(self):
        pass

    def MakeShallowCopy(self):
        pass

    def MergeAdditionalChannels(self):
        pass

    def NewAndCopyChannels(self):
        pass

    def NormalAlignVector(self):
        pass

    def PointSelection(self):
        pass

    def PointsWereChanged(self):
        pass

    def PreferredCollapseType(self):
        pass

    def ReadyChannelsForMod(self):
        pass

    def ReduceCaches(self):
        pass

    def SetChannelLocks(self):
        pass

    def SetChannelValidity(self):
        pass

    def SetNoEvalInterval(self):
        pass

    def SetPoint(self):
        pass

    def SetSubSelState(self):
        pass

    def SetWeight(self):
        pass

    def ShallowCopy(self):
        pass

    def SurfaceClosedU(self):
        pass

    def SurfaceClosedV(self):
        pass

    def TopologyChanged(self):
        pass

    def UnlockChannels(self):
        pass

    def UnlockObject(self):
        pass

    def UpdateValidity(self):
        pass

    def UseSelectionBrackets(self):
        pass

    def UsesWireColor(self):
        pass

    def WSStateInvalidate(self):
        pass


class CameraObject(Object):
    thisown = ()
    def EvalCameraState(self):
        pass

    def GetClipDist(self):
        pass

    def GetEnvDisplay(self):
        pass

    def GetEnvRange(self):
        pass

    def GetFOV(self):
        pass

    def GetManualClip(self):
        pass

    def GetMultiPassCameraEffect(self):
        pass

    def GetMultiPassEffectEnabled(self):
        pass

    def GetMultiPassEffectPerPass(self):
        pass

    def GetTDist(self):
        pass

    def IsOrtho(self):
        pass

    def RenderApertureChanged(self):
        pass

    def SetClipDist(self):
        pass

    def SetEnvDisplay(self):
        pass

    def SetEnvRange(self):
        pass

    def SetFOV(self):
        pass

    def SetManualClip(self):
        pass

    def SetMultiPassCameraEffect(self):
        pass

    def SetMultiPassEffectEnabled(self):
        pass

    def SetMultiPassEffectPerPass(self):
        pass

    def SetOrtho(self):
        pass

    def SetTDist(self):
        pass

    def UpdateTargDistance(self):
        pass


class GeomObject(Object):
    thisown = ()
    def CanDoDisplacementMapping(self):
        pass

    def IsInstanceDependent(self):
        pass

    def NumberOfRenderMeshes(self):
        pass



class HelperObject(Object):
    thisown = ()


class IDerivedObject(Object):
    thisown = ()
    def AddModifier(self):
        pass

    def DeleteModifier(self):
        pass

    def Eval(self):
        pass

    def GetModContext(self):
        pass

    def GetModifier(self):
        pass

    def GetNumModifiers(self):
        pass

    def GetObjRef(self):
        pass

    def ReferenceObject(self):
        pass

    def SetModifier(self):
        pass


class LightObject(Object):
    thisown = ()
    def Enable(self):
        pass

    def Eval(self):
        return RefResult()

    def GetAbsMapBias(self):
        pass

    def GetAspect(self):
        pass

    def GetAtten(self):
        pass

    def GetAttenDisplay(self):
        pass

    def GetConeDisplay(self):
        pass

    def GetFallsize(self):
        pass

    def GetHotspot(self):
        pass

    def GetIntensity(self):
        pass

    def GetMapBias(self):
        pass

    def GetMapRange(self):
        pass

    def GetMapSize(self):
        pass

    def GetOvershoot(self):
        pass

    def GetProjector(self):
        pass

    def GetProjMap(self):
        return TexMap()

    def GetRayBias(self):
        pass

    def GetRGBColor(self):
        return Point3()

    def GetShadow(self):
        pass

    def GetShadowMethod(self):
        pass

    def GetShadowType(self):
        pass

    def GetTDist(self):
        pass

    def GetUseAtten(self):
        pass

    def GetUseGlobal(self):
        pass

    def GetUseLight(self):
        pass

    def SetAbsMapBias(self):
        pass

    def SetAspect(self):
        pass

    def SetAtten(self):
        pass

    def SetAttenDisplay(self):
        pass

    def SetConeDisplay(self):
        pass

    def SetFallsize(self):
        pass

    def SetHotspot(self):
        pass

    def SetIntensity(self):
        pass

    def SetMapBias(self):
        pass

    def SetMapRange(self):
        pass

    def SetMapSize(self):
        pass

    def SetOvershoot(self):
        pass

    def SetProjector(self):
        pass

    def SetProjMap(self):
        pass

    def SetRayBias(self):
        pass

    def SetRGBColor(self):
        pass

    def SetShadow(self):
        pass

    def SetShadowType(self):
        pass

    def SetTDist(self):
        pass

    def SetUseAtten(self):
        pass

    def SetUseGlobal(self):
        pass

    def SetUseLight(self):
        pass

    def UpdateTargDistance(self):
        pass


class GenCamera(CameraObject):
    thisown = ()
    def Enable(self):
        pass

    def GetCameraType(self):
        pass

    def GetConeState(self):
        pass

    def GetDOFEnable(self):
        pass

    def GetDOFFStop(self):
        pass

    def GetFOVControl(self):
        pass

    def GetFOVType(self):
        pass

    def GetHorizontalLineState(self):
        pass

    def NewCamera(self):
        pass

    def SetCameraType(self):
        pass

    def SetConeState(self):
        pass

    def SetDOFEnable(self):
        pass

    def SetDOFFStop(self):
        pass

    def SetFOVControl(self):
        pass

    def SetFOVType(self):
        pass

    def SetHorizontalLineState(self):
        pass


class PolyObject(GeomObject):
    thisown = ()


class ShapeObject(GeomObject):
    thisown = ()
    def AttachShape(self):
        pass

    def CanMakeBezier(self):
        pass

    def CopyBaseData(self):
        pass

    def CurveClosed(self):
        pass

    def GenerateMesh(self):
        pass

    def GetAngle(self):
        pass

    def GetDispRenderMesh(self):
        pass

    def GetGenUVs(self):
        pass

    def GetLengthOfCurve(self):
        pass

    def GetMatID(self):
        return MtlID()

    def GetNumberOfCurves(self):
        pass

    def GetNumberOfPieces(self):
        pass

    def GetNumberOfVertices(self):
        pass

    def GetObjectDisplayRequirement(self):
        pass

    def GetRenderable(self):
        pass

    def GetShapeObjValidity(self):
        return Interval()

    def GetSides(self):
        pass

    def GetThickness(self):
        pass

    def GetUsePhysicalScaleUVs(self):
        pass

    def GetUseViewport(self):
        pass

    def GetViewportAngle(self):
        pass

    def GetViewportOrRenderer(self):
        pass

    def GetViewportSides(self):
        pass

    def GetViewportThickness(self):
        pass

    def InterpCurve3D(self):
        return Point3()

    def InterpPiece3D(self):
        return Point3()

    def MakeBezier(self):
        pass

    def MakePolyShape(self):
        pass

    def PrepareDisplay(self):
        pass

    def SetAngle(self):
        pass

    def SetDispRenderMesh(self):
        pass

    def SetGenUVs(self):
        pass

    def SetRenderable(self):
        pass

    def SetSides(self):
        pass

    def SetThickness(self):
        pass

    def SetUsePhysicalScaleUVs(self):
        pass

    def SetUseViewport(self):
        pass

    def SetViewportAngle(self):
        pass

    def SetViewportOrRenderer(self):
        pass

    def SetViewportSides(self):
        pass

    def SetViewportThickness(self):
        pass

    def TangentCurve3D(self):
        return Point3()

    def TangentPiece3D(self):
        return Point3()

    def UpdatePerNodeItems(self):
        pass

    def UpdatePerViewItems(self):
        pass


class TriObject(GeomObject):
    GetNumTriFaces = ()

    GetNumTriVerts = ()

    thisown = ()

    def ApplyUVWMap(self):
        pass

    def ChannelValidity(self):
        pass

    def CheckObjectIntegrity(self):
        pass

    def ConvertValidity(self):
        pass

    def CreateTriObjRep(self):
        pass

    def Eval(self):
        pass

    def FreeChannels(self):
        pass

    def GetDeformBBox(self):
        pass

    def GetDisableDisplacement(self):
        pass

    def GetMesh(self):
        pass

    def GetNumMapChannels(self):
        pass

    def GetNumMapsUsed(self):
        pass

    def GetNumTriFaces(self):
        pass

    def GetNumTriVerts(self):
        pass

    def GetObjectDisplayRequirement(self):
        pass

    def GetSplitMeshForDisplacement(self):
        pass

    def GetSubDivideDisplacement(self):
        pass

    def GetSubselState(self):
        pass

    def HasUVW(self):
        pass

    def InvalidateChannels(self):
        pass

    def IsMappable(self):
        pass

    def IsPointSelected(self):
        pass

    def MakeShallowCopy(self):
        pass

    def NewAndCopyChannels(self):
        pass

    def PointSelection(self):
        pass

    def PointsWereChanged(self):
        pass

    def PrepareDisplay(self):
        pass

    def SetChannelValidity(self):
        pass

    def SetDisableDisplacement(self):
        pass

    def SetDisplacmentApproxToPreset(self):
        pass

    def SetSplitMeshForDisplacement(self):
        pass

    def SetSubDivideDisplacement(self):
        pass

    def SetSubSelState(self):
        pass

    def ShallowCopy(self):
        pass

    def TopologyChanged(self):
        pass

    def UpdatePerNodeItems(self):
        pass

    def UpdatePerViewItems(self):
        pass


class ConstObject(HelperObject):
    thisown = ()
    def GetConstructionPlane(self):
        pass

    def GetConstructionTM(self):
        pass

    def GetExtents(self):
        pass

    def GetSnaps(self):
        pass

    def IsConstObject(self):
        pass

    def IsTemporary(self):
        pass

    def IsTransient(self):
        pass

    def SetConstructionPlane(self):
        pass

    def SetExtents(self):
        pass

    def SetSnaps(self):
        pass

    def SetTemporary(self):
        pass

    def SetTransient(self):
        pass


class DummyObject(HelperObject):
    thisown = ()
    def DisableDisplay(self):
        pass

    def EnableDisplay(self):
        pass

    def GetBox(self):
        pass

    def SetBox(self):
        pass

    def SetColor(self):
        pass

    def SetValidity(self):
        pass


class GizmoObject(HelperObject):
    thisown = ()


class GenLight(LightObject):
    thisown = ()
    def GetAffectDiffuse(self):
        pass

    def GetAffectSpecular(self):
        pass

    def GetAmbientOnly(self):
        pass

    def GetAtmosColAmt(self):
        pass

    def GetAtmosOpacity(self):
        pass

    def GetAtmosShadows(self):
        pass

    def GetAttenNearDisplay(self):
        pass

    def GetColorControl(self):
        pass

    def GetConeDisplay(self):
        pass

    def GetContrast(self):
        pass

    def GetDecayRadius(self):
        pass

    def GetDecayType(self):
        pass

    def GetDiffuseSoft(self):
        pass

    def GetFalloffControl(self):
        pass

    def GetHotSpotControl(self):
        pass

    def GetLightAffectsShadow(self):
        pass

    def GetLightType(self):
        pass

    def GetOvershoot(self):
        pass

    def GetShadColor(self):
        pass

    def GetShadMult(self):
        pass

    def GetShadowProjMap(self):
        pass

    def GetUseAttenNear(self):
        pass

    def GetUseShadowColorMap(self):
        pass

    def IsDir(self):
        pass

    def IsSpot(self):
        pass

    def SetAbsMapBias(self):
        pass

    def SetAffectDiffuse(self):
        pass

    def SetAffectSpecular(self):
        pass

    def SetAmbientOnly(self):
        pass

    def SetAtmosColAmt(self):
        pass

    def SetAtmosOpacity(self):
        pass

    def SetAtmosShadows(self):
        pass

    def SetAttenNearDisplay(self):
        pass

    def SetColorControl(self):
        pass

    def SetConeDisplay(self):
        pass

    def SetContrast(self):
        pass

    def SetDecayRadius(self):
        pass

    def SetDecayType(self):
        pass

    def SetDiffuseSoft(self):
        pass

    def SetFalloffControl(self):
        pass

    def SetHotSpotControl(self):
        pass

    def SetLightAffectsShadow(self):
        pass

    def SetLightType(self):
        pass

    def SetOvershoot(self):
        pass

    def SetShadColor(self):
        pass

    def SetShadMult(self):
        pass

    def SetShadowProjMap(self):
        pass

    def SetUseAttenNear(self):
        pass

    def SetUseShadowColorMap(self):
        pass


class AColor(Wrapper):
    AComp = ()
    CompositeOver = ()
    def AComp(self):
        pass

    def Black(self):
        pass

    def ClampMax(self):
        pass

    def ClampMin(self):
        pass

    def ClampMinMax(self):
        pass

    def CompositeOver(self):
        pass

    def GetA(self):
        pass

    def GetB(self):
        pass

    def GetG(self):
        pass

    def GetIntensity(self):
        pass

    def GetR(self):
        pass

    def SetA(self):
        pass

    def SetB(self):
        pass

    def SetG(self):
        pass

    def SetR(self):
        pass

    def ToRGB(self):
        pass

    def White(self):
        pass


class AColorList:
    this = ()
    thisown = ()
    def Append(self):
        pass

    def Delete(self):
        pass

    def GetCount(self):
        pass

    def GetItem(self):
        pass

    def Insert(self):
        pass

    def SetCount(self):
        pass

    def SetItem(self):
        pass


class ActionContext(Wrapper):
    Active = ()
    Id = ()
    Name = ()
    def  GetContextId (self):
        pass

    def  GetName (self):
        pass

    def  IsActive (self):
        pass

    def  SetActive (self):
        pass


class ActionFactory:
    ActionItems = []
    CustomActionItems = []

    def Create(self, category, name, fxn):
        pass

    def CreateFromAbstract(self, item):
        pass


class ActionItem(FPInterface):
    ButtonText = ()

    Category = ()

    Checked = ()

    Description = ()

    Dynamic = ()

    Enabled = ()

    Id = ()

    Indeterminate = ()

    MenuText = ()

    Shortcut = ()

    thisown = ()

    Visible = ()

    def Execute(self):
        pass

    def ExecuteAction(self):
        pass

    def GetButtonText(self):
        pass

    def GetCategoryText(self):
        pass

    def GetDescriptionText(self):
        pass

    def GetId(self):
        pass

    def GetIsChecked(self):
        pass

    def GetIsDynamicAction(self):
        pass

    def GetIsEnabled(self):
        pass

    def GetIsIndeterminate(self):
        pass

    def GetIsItemVisible(self):
        pass

    def GetMenuText(self):
        pass

    def GetShortcutString(self):
        pass


class ActionManager:
    ActionContexts = ()

    ActionTables = ()

    FindContext = ()

    GetActionContext = ()

    GetActionTable = ()

    GetFPStaticInterface = ()

    GetKeyboardFile = ()

    GetNumActionContexts = ()

    GetNumActionTables = ()

    GetShortcutDir = ()

    GetShortcutFile = ()

    IdToIndex = ()

    IsContextActive = ()

    LoadKeyboardFile = ()

    MakeActionSetCurrent = ()

    RegisterActionContext = ()

    SaveAllContextsToINI = ()

    SaveKeyboardFile = ()

    thisown = ()

    def FindContext(self):
        pass

    def FindTable(self):
        pass

    def GetActionContext(self):
        pass

    def GetActionTable(self):
        pass

    def GetFPStaticInterface(self):
        pass

    def GetKeyboardFile(self):
        pass

    def GetNumActionContexts(self):
        pass

    def GetNumActionTables(self):
        pass

    def GetShortcutDir(self):
        pass

    def GetShortcutFile(self):
        pass

    def IdToIndex(self):
        pass

    def IsContextActive(self):
        pass

    def LoadKeyboardFile(self):
        pass

    def MakeActionSetCurrent(self):
        pass

    def RegisterActionContext(self):
        pass

    def RegisterActionTable(self):
        pass

    def SaveAllContextsToINI(self):
        pass

    def SaveKeyboardFile(self):
        pass


class ActionTable(FPInterface):
    Actions = ()

    NumActions = ()

    thisown = ()

    def GetAction(self):
        pass

    def GetNumActions(self):
        pass


class AffineParts(Wrapper):
    this = ()
    thisown = ()
    def GetF(self):
        pass

    def GetK(self):
        pass

    def GetQ(self):
        pass

    def GetT(self):
        pass

    def GetU(self):
        pass


class AngAxis(Wrapper):
    Angle = ()
    Axis = ()
    NumRevs = ()
    def GetAngle(self):
        pass

    def GetAxis(self):
        pass

    def GetNumRevs(self):
        pass

    def Set(self):
        pass

    def SetAngle(self):
        pass

    def SetAxis(self):
        pass

    def SetNumRevs(self):
        pass


class AngAxisList:
    this = ()
    thisown = ()
    def Append(self):
        pass

    def Delete(self):
        pass

    def GetCount(self):
        pass

    def GetItem(self):
        pass

    def Insert(self):
        pass

    def SetCount(self):
        pass

    def SetItem(self):
        pass


class AnimatableInterfaceIds:
    IAggregation = 0

    IBaseobject = 0

    IComponent = 0

    ICompositesubmtlapi = 0

    IDerivedobject = 0

    IEaselist = 0

    IEulerctrl = 0

    IGeomimp = 0

    IGuest = 0

    IHost = 0

    IIkchaincontrol = 0

    IIkcontrol = 0

    IKeycontrol = 0

    IKeycontrol2 = 0

    ILightobj = 0

    ILinktmctrl = 0

    ILocked = 0

    ILockedClient = 0

    IMaster = 0

    IMaxscriptplugin = 0

    IMentalray = 0

    IMeshdeltauser = 0

    IMeshdeltauserdata = 0

    IMeshselect = 0

    IMeshselectdata = 0

    IMitranslator = 0

    IMtlidset = 0

    IMultitangent = 0

    IMultlist = 0

    INewmtlinterface = 0

    INewpartoperator = 0

    INewpartpod = 0

    INewpartsource = 0

    INewparttest = 0

    IObject = 0

    IObjectsuperclassNotObjectclass = 0

    IParticleobj = 0

    IPatchops = 0

    IPatchselect = 0

    IPatchselectdata = 0

    IReagent = 0

    IRefarray = 0

    ISceneobject = 0

    IScriptcontrol = 0

    ISetkeycontrol = 0

    ISimpleparticleobj = 0

    ISoftselect = 0

    ISplineops = 0

    ISplineselect = 0

    ISplineselectdata = 0

    ISubmap = 0

    ISubtargetctrl = 0

    ISystemXref = 0

    ITextobject = 0

    IUnreplaceablectl = 0

    IUserinterface = 0

    IValence = 0

    IWavesound = 0

    IWirecontrol = 0

    IWsmobject = 0



class Animation:
    AreWeKeying = ()

    EnableAnimateButton = ()

    EndPlayback = ()

    GetAnimRange = ()

    GetAutoKeyDefaultKeyOn = ()

    GetAutoKeyDefaultKeyTime = ()

    GetControllerOverrideRangeDefault = ()

    GetDefaultInTangentType = ()

    GetDefaultOutTangentType = ()

    GetEndTime = ()

    GetIsAnimating = ()

    GetPlayActiveOnly = ()

    GetPlaybackLoop = ()

    GetPlaybackSpeed = ()

    GetRealTimePlayback = ()

    GetSetKeyMode = ()

    GetSetKeyModeStatus = ()

    GetSetKeySuspended = ()

    GetStartTime = ()

    GetTime = ()

    IsAnimateEnabled = ()

    IsPlaying = ()

    IsSetKeyModeFeatureEnabled = ()

    ResumeAnimate = ()

    ResumeSetKeyMode = ()

    SetAnimateButtonState = ()

    SetAutoKeyDefaultKeyOn = ()

    SetAutoKeyDefaultKeyTime = ()

    SetControllerOverrideRangeDefault = ()

    SetDefaultTangentType = ()

    SetEndTime = ()

    SetIsAnimating = ()

    SetPlayActiveOnly = ()

    SetPlaybackLoop = ()

    SetPlaybackSpeed = ()

    SetRange = ()

    SetRealTimePlayback = ()

    SetSetKeyMode = ()

    SetStartTime = ()

    SetTime = ()

    StartPlayback = ()

    SuspendAnimate = ()

    SuspendSetKeyMode = ()

    thisown = ()

    def AreWeKeying(self, TimeValue):
        pass

    def EnableAnimateButton(self,bool):
        pass

    def EndPlayback(self):
        pass

    def GetAnimRange(self):
        return Interval()

    def GetAutoKeyDefaultKeyOn(self):
        return True

    def GetAutoKeyDefaultKeyTime(self):
        return TimeValue()

    def GetControllerOverrideRangeDefault(self):
        return True

    def GetDefaultInTangentType(self):
        return 0

    def GetDefaultOutTangentType(self):
        return 0

    def GetEndTime(self):
        return TimeValue()

    def GetIsAnimating(self):
        return True

    def GetPlayActiveOnly(self):
        return True

    def GetPlaybackLoop(self):
        return True

    def GetPlaybackSpeed(self):
        return 0

    def GetRealTimePlayback(self):
        return True

    def GetSetKeyMode(self):
        return True

    def GetSetKeyModeStatus(self):
        return True

    def GetSetKeySuspended(self):
        return True

    def GetStartTime(self):
        return TimeValue()

    def GetTime(self):
        return TimeValue()

    def IsAnimateEnabled(self):
        return True

    def IsPlaying(self):
        return True

    def IsSetKeyModeFeatureEnabled(self):
        return True

    def ResumeAnimate(self):
        pass

    def ResumeSetKeyMode(self):
        pass

    def SetAnimateButtonState(self, bool):
        pass

    def SetAutoKeyDefaultKeyOn(self, bool):
        pass

    def SetAutoKeyDefaultKeyTime(self, TimeValue):
        pass

    def SetControllerOverrideRangeDefault(self, bool):
        pass

    def SetDefaultTangentType(self, dfltInTangenttype, dfltOutTangentType, bool):
        pass

    def SetEndTime(self, TimeValue):
        pass

    def SetIsAnimating(self, bool):
        pass

    def SetPlayActiveOnly(self, bool):
        pass

    def SetPlaybackLoop(self, bool):
        pass

    def SetPlaybackSpeed(self, int):
        pass

    def SetRange(self, Interval):
        pass

    def SetRealTimePlayback(self, bool):
        pass

    def SetSetKeyMode(self, bool):
        pass

    def SetStartTime(self, TimeValue):
        pass

    def SetTime(self, TimeValue, bool):
        pass

    def StartPlayback(self, bool):
        pass

    def SuspendAnimate(self):
        pass

    def SuspendSetKeyMode(self):
        pass


class AnimationKeySteps:
    GetPosition = ()

    GetRotation = ()

    GetScale = ()

    GetSelectedOnly = ()

    GetUseTrackBar = ()

    GetUseTransform = ()

    SetPosition = ()

    SetRotation = ()

    SetScale = ()

    SetSelectedOnly = ()

    SetUseTrackBar = ()

    SetUseTransform = ()

    thisown = ()

    def GetPosition(self):
        pass

    def GetRotation(self):
        pass

    def GetScale(self):
        pass

    def GetSelectedOnly(self):
        pass

    def GetUseTrackBar(self):
        pass

    def GetUseTransform(self):
        pass

    def SetPosition(self):
        pass

    def SetRotation(self):
        pass

    def SetScale(self):
        pass

    def SetSelectedOnly(self):
        pass

    def SetUseTrackBar(self):
        pass

    def SetUseTransform(self):
        pass


class AnimationTrajectory:
    DeleteSelectedKey = ()

    GetAddKeyMode = ()

    GetKeySubMode = ()

    GetMode = ()

    SetAddKeyMode = ()

    SetKeySubMode = ()

    SetMode = ()

    thisown = ()

    def DeleteSelectedKey(self):
        pass

    def GetAddKeyMode(self):
        pass

    def GetKeySubMode(self):
        pass

    def GetMode(self):
        pass

    def SetAddKeyMode(self):
        pass

    def SetKeySubMode(self):
        pass

    def SetMode(self):
        pass


class Application:
    AutoBackupEnabled = ()

    CheckMAXMessages = ()

    DrawingEnabled = ()

    EnableAutoBackup = ()

    EnableDrawing = ()

    ExecuteMAXCommand = ()

    FlushUndoBuffer = ()

    Get3DSMAXVersion = ()

    GetAppID = ()

    GetAutoBackupTime = ()

    GetInterface = ()

    GetLicenseBehavior = ()

    GetLicenseDaysLeft = ()

    GetProductVersion = ()

    GetQuietMode = ()

    GetScreenHeight = ()

    GetScreenWidth = ()

    GetSoundObject = ()

    IsDebugging = ()

    IsFeatureLicensed = ()

    IsNetworkLicense = ()

    IsQuitingApp = ()

    IsSceneResetting = ()

    IsTrialLicense = ()

    IsUsingProfileDirectories = ()

    IsUsingRoamingProfiles = ()

    NumberOfProcessors = ()

    RescaleWorldUnits = ()

    SetAutoBackupTime = ()

    SetQuietMode = ()

    SetSoundObject = ()

    thisown = ()

    def AutoBackupEnabled(self):
        pass

    def CheckMAXMessages(self):
        pass

    def DrawingEnabled(self):
        pass

    def EnableAutoBackup(self):
        pass

    def EnableDrawing(self):
        pass

    def ExecuteMAXCommand(self):
        pass

    def FlushUndoBuffer(self):
        pass

    def Get3DSMAXVersion(self):
        pass

    def GetAppID(self):
        pass

    def GetAutoBackupTime(self):
        pass

    def GetInterface(self):
        pass

    def GetLicenseBehavior(self):
        pass

    def GetLicenseDaysLeft(self):
        pass

    def GetProductVersion(self):
        pass

    def GetQuietMode(self):
        pass

    def GetScreenHeight(self):
        pass

    def GetScreenWidth(self):
        pass

    def GetSoundObject(self):
        pass

    def IsDebugging(self):
        pass

    def IsFeatureLicensed(self):
        pass

    def IsNetworkLicense(self):
        pass

    def IsQuitingApp(self):
        pass

    def IsSceneResetting(self):
        pass

    def IsTrialLicense(self):
        pass

    def IsUsingProfileDirectories(self):
        pass

    def IsUsingRoamingProfiles(self):
        pass

    def NumberOfProcessors(self):
        pass

    def RescaleWorldUnits(self):
        pass

    def SetAutoBackupTime(self):
        pass

    def SetQuietMode(self):
        pass

    def SetSoundObject(self):
        pass


class ArrayParameter:
    IsAnimatable = ()

    IsArrayData = ()

    IsArrayParameter = ()

    IsObsolete = ()

    IsReadOnly = ()

    IsResizable = ()

    Items = ()

    Name = ()

    NumItems = ()

    thisown = ()

    Type = ()

    Value = ()

    def Append(self):
        pass

    def Count(self):
        pass

    def Delete(self):
        pass

    def GetController(self):
        pass

    def GetItem(self):
        pass

    def GetName(self):
        pass

    def GetType(self):
        pass

    def GetValue(self):
        pass

    def Insert(self):
        pass

    def IsAnimatable(self):
        pass

    def IsArrayData(self):
        pass

    def IsArrayParameter(self):
        pass

    def IsObsolete(self):
        pass

    def IsReadOnly(self):
        pass

    def IsResizable(self):
        pass

    def ReplaceController(self):
        pass

    def SetController(self):
        pass

    def SetCount(self):
        pass

    def SetValue(self):
        pass


class Asset(Wrapper):
    ResolvedFileName = ()
    SpecifiedFileName = ()
    Type = ()
    def GetAssetType(self):
        pass
    def GetResolvedFileName(self):
        pass
    def GetSpecifiedFileName(self):
        pass


class AssetDirectories:
    Add = ()

    AddSession = ()

    Delete = ()

    DeleteSession = ()

    Get = ()

    GetCount = ()

    GetCurrent = ()

    GetCurrentCount = ()

    GetSession = ()

    GetSessionCount = ()

    thisown = ()

    UpdateSection = ()

    def Add(self):
        pass

    def AddSession(self):
        pass

    def Delete(self):
        pass

    def DeleteSession(self):
        pass

    def Get(self):
        pass

    def GetCount(self):
        pass

    def GetCurrent(self):
        pass

    def GetCurrentCount(self):
        pass

    def GetSession(self):
        pass

    def GetSessionCount(self):
        pass

    def UpdateSection(self):
        pass


class AssetManager:
    CreateAsset = ()
    GetAssets = ()
    thisown = ()
    def CreateAsset(self, filename, assetType):
        return Asset()
    def GetAssets(self, flags):
        return AssetTuple()


class AssetTuple:
    thisown = ()

    def At(self):
        pass

    def GetCount(self):
        pass


class AssetType:
    thisown = ()
    AnimationAsset = 0
    BatchRender = 0
    BitmapAsset = 0
    ContainerAsset = 0
    ExternalLink = 0
    OtherAsset = 0
    PhotometricAsset = 0
    PostRenderScript = 0
    PredefinedAssetTypeCount = 0
    PreRenderScript = 0
    RenderOutput = 0
    SoundAsset = 0
    VideoPost = 0
    XRefAsset = 0


class Atmospheric:
    thisown = ()


class Atomspherics:
    Add = ()
    Delete = ()
    Edit = ()
    Get = ()
    GetCount = ()
    Set = ()
    thisown = ()

    def Add(self, Atmospheric):
        pass

    def Delete(self, int):
        pass

    def Edit(self,Atmospheric,INode):
        pass

    def Get(self,int):
        return Atmospheric()

    def GetCount(self):
        return 0

    def Set(self,int,Atmospheric):
        pass


class Axis:
    EnableConstraints = ()

    GetConstantRestriction = ()

    GetConstraints = ()

    GetCount = ()

    GetTransformAxis = ()

    GetTripodLocked = ()

    PopConstraints = ()

    PushConstraints = ()

    SetConstantRestriction = ()

    SetConstraints = ()

    SetLockTripods = ()

    thisown = ()

    def EnableConstraints(self):
        pass

    def GetConstantRestriction(self):
        pass

    def GetConstraints(self):
        pass

    def GetCount(self):
        pass

    def GetTransformAxis(self):
        pass

    def GetTripodLocked(self):
        pass

    def PopConstraints(self):
        pass

    def PushConstraints(self):
        pass

    def SetConstantRestriction(self):
        pass

    def SetConstraints(self):
        pass

    def SetLockTripods(self):
        pass


class BezierShapeTopology(Wrapper):
    thisown = ()
    def Equals(self):
        pass

    def GetClosed(self):
        pass

    def GetKCount(self):
        pass

    def GetReady(self):
        pass


class BitArray(Wrapper):
    this = ()
    kMAX_LOCALBITS = ()
    def AnyBitSet(self):
        pass

    def Clear(self):
        pass

    def ClearAll(self):
        pass

    def Compress(self):
        pass

    def DeleteSet(self):
        pass

    def Expand(self):
        pass

    def GetSize(self):
        pass

    def IsEmpty(self):
        pass

    def kMAX_LOCALBITS(self):
        pass

    def Reverse(self):
        pass

    def Rotate(self):
        pass

    def Set(self):
        pass

    def SetAll(self):
        pass

    def SetSize(self):
        pass

    def Shift(self):
        pass

    def Swap(self):
        pass


class BitArrayList:
    this = ()
    thisown = ()

    def Append(self):
        pass

    def Delete(self):
        pass

    def GetCount(self):
        pass

    def GetItem(self):
        pass

    def Insert(self):
        pass

    def SetCount(self):
        pass

    def SetItem(self):
        pass


class BitmapInfo(Wrapper):
    thisown = ()
    def AllocProxySubject(self):
        pass

    def CompareName(self):
        pass

    def Copy(self):
        pass

    def CopyImageInfo(self):
        pass

    def EndFrame(self):
        pass

    def GetAspectRatio(self):
        pass

    def GetAsset(self):
        pass

    def GetCurrentFrame(self):
        pass

    def GetCustHeight(self):
        pass

    def GetCustomFlags(self):
        pass

    def GetCustomGamma(self):
        pass

    def GetCustomStep(self):
        pass

    def GetCustomX(self):
        pass

    def GetCustomY(self):
        pass

    def GetCustWidth(self):
        pass

    def GetDevice(self):
        pass

    def GetEffectiveGamma(self):
        pass

    def GetFileName(self):
        pass

    def GetFirstFrame(self):
        pass

    def GetFlags(self):
        pass

    def GetGamma(self):
        pass

    def GetHeight(self):
        pass

    def GetLastFrame(self):
        pass

    def GetName(self):
        pass

    def GetNumberFrames(self):
        pass

    def GetPathEx(self):
        pass

    def GetPresetAlignment(self):
        pass

    def GetProxySubject(self):
        pass

    def GetSequenceOutBound(self):
        pass

    def GetType(self):
        pass

    def GetWidth(self):
        pass

    def ResetCustomFlag(self):
        pass

    def ResetFlags(self):
        pass

    def ResetProxySubject(self):
        pass

    def SetAspect(self):
        pass

    def SetAsset(self):
        pass

    def SetCurrentFrame(self):
        pass

    def SetCustHeight(self):
        pass

    def SetCustomFlag(self):
        pass

    def SetCustomGamma(self):
        pass

    def SetCustomStep(self):
        pass

    def SetCustomX(self):
        pass

    def SetCustomY(self):
        pass

    def SetCustWidth(self):
        pass

    def SetDevice(self):
        pass

    def SetEndFrame(self):
        pass

    def SetFirstFrame(self):
        pass

    def SetFlags(self):
        pass

    def SetGamma(self):
        pass

    def SetHeight(self):
        pass

    def SetLastFrame(self):
        pass

    def SetName(self):
        pass

    def SetPath(self):
        pass

    def SetPresetAlignment(self):
        pass

    def SetSequenceOutBound(self):
        pass

    def SetStartFrame(self):
        pass

    def SetType(self):
        pass

    def SetWidth(self):
        pass

    def StartFrame(self):
        pass

    def TestCustomFlags(self):
        pass

    def TestFlags(self):
        pass

    def Validate(self):
        pass


class BitmapList:
    this = ()
    thisown = ()

    def Append(self):
        pass

    def Delete(self):
        pass

    def GetCount(self):
        pass

    def GetItem(self):
        pass

    def Insert(self):
        pass

    def SetCount(self):
        pass

    def SetItem(self):
        pass


class BitmapManager:
    CanImport = ()

    FreeSceneBitmaps = ()

    GetImageInfo = ()

    GetImageInfoDlg = ()

    GetImageInputOptions = ()

    GetSilentMode = ()

    Load = ()

    SelectDeviceInput = ()

    SelectDeviceOutput = ()

    SelectFileInputEx = ()

    SelectFileOutput = ()

    SetSilentMode = ()

    thisown = ()

    def CanImport(self):
        pass

    def FreeSceneBitmaps(self):
        pass

    def GetImageInfo(self):
        pass

    def GetImageInfoDlg(self):
        pass

    def GetImageInputOptions(self):
        pass

    def GetSilentMode(self):
        pass

    def Load(self):
        pass

    def SelectDeviceInput(self):
        pass

    def SelectDeviceOutput(self):
        pass

    def SelectFileInputEx(self):
        pass

    def SelectFileOutput(self):
        pass

    def SetSilentMode(self):
        pass


class BitmapTex(Texmap):
    thisown = ()

    def BitmapLoadDlg(self):
        pass

    def GetAlphaAsMono(self):
        pass

    def GetAlphaAsRGB(self):
        pass

    def GetAlphaSource(self):
        pass

    def GetBitmap(self):
        pass

    def GetEndCondition(self):
        pass

    def GetFilterType(self):
        pass

    def GetMap(self):
        pass

    def GetMapName(self):
        pass

    def GetPlaybackRate(self):
        pass

    def GetPremultAlpha(self):
        pass

    def GetStartTime(self):
        pass

    def ReloadBitmapAndUpdate(self):
        pass

    def SetAlphaAsMono(self):
        pass

    def SetAlphaAsRGB(self):
        pass

    def SetAlphaSource(self):
        pass

    def SetBitmap(self):
        pass

    def SetEndCondition(self):
        pass

    def SetFilterType(self):
        pass

    def SetMap(self):
        pass

    def SetMapName(self):
        pass

    def SetPlaybackRate(self):
        pass

    def SetPremultAlpha(self):
        pass

    def SetStartTime(self):
        pass


class BoolList:
    this = ()
    thisown = ()

    def Append(self):
        pass

    def Delete(self):
        pass

    def GetCount(self):
        pass

    def GetItem(self):
        pass

    def Insert(self):
        pass

    def SetCount(self):
        pass

    def SetItem(self):
        pass


class Box2(Wrapper):
    H = ()
    W = ()
    X = ()
    Y = ()
    def Contains(self):
        pass

    def GetCenter(self):
        pass

    def GetH(self):
        pass

    def GetMax(self):
        pass

    def GetMin(self):
        pass

    def GetW(self):
        pass

    def GetX(self):
        pass

    def GetY(self):
        pass

    def IsEmpty(self):
        pass

    def Rectify(self):
        pass

    def Scale(self):
        pass

    def SetEmpty(self):
        pass

    def SetH(self):
        pass

    def SetW(self):
        pass

    def SetWH(self):
        pass

    def SetX(self):
        pass

    def SetXY(self):
        pass

    def SetY(self):
        pass

    def Translate(self):
        pass


class Box3:
    this = ()
    Center = ()
    Max = ()
    Min = ()
    Width = ()
    def Contains

    def EnlargeBy

    def GetCenter

    def GetMax

    def GetMin

    def GetWidth

    def IncludePoint

    def Init

    def Intersects

    def IsEmpty

    def MakeCube

    def Scale

    def Transform(self):
        pass

    def Translate(self):
        pass


class CameraState(Wrapper):
    thisown = ()
    def GetFov(self):
        pass

    def GetHither(self):
        pass

    def GetHorzLine(self):
        pass

    def GetIsOrtho(self):
        pass

    def GetManualClip(self):
        pass

    def GetNearRange(self):
        pass

    def GetRarRange(self):
        pass

    def GetTDist(self):
        pass

    def GetYon(self):
        pass


class Class_ID(Wrapper):
    this = ()
    def GetPartA(self):
        pass

    def GetPartB(self):
        pass

    def SetPartA(self):
        pass

    def SetPartB(self):
        pass


class ClassDesc(Wrapper):
    thisown = ()
    def AddInterface(self):
        pass

    def ClearInterfaces(self):
        pass

    def EditClassParams(self):
        pass

    def GetCategory(self):
        pass

    def GetClassID(self):
        pass

    def GetClassName(self):
        pass

    def GetInterface(self):
        pass

    def GetInterfaceAt(self):
        pass

    def GetInternalName(self):
        pass

    def GetNeedsToSave(self):
        pass

    def GetNumActionTables(self):
        pass

    def GetNumInterfaces(self):
        pass

    def GetNumParamBlockDescs(self):
        pass

    def GetParamBlockDesc(self):
        pass

    def GetResourceString(self):
        pass

    def GetSubClassID(self):
        pass

    def GetSuperClassID(self):
        pass

    def HasClassParams(self):
        pass

    def IsPublic(self):
        pass

    def ResetClassParams(self):
        pass


class ClassDescList:
    this = ()
    thisown = ()
    def Append(self):
        pass

    def Delete(self):
        pass

    def GetCount(self):
        pass

    def GetItem(self):
        pass

    def Insert(self):
        pass

    def SetCount(self):
        pass

    def SetItem(self):
        pass


class ClassIds:
    Sphere = ()
    Box = ()
    Cylinder = ()
    Torus = ()
    Bend = ()
    Cone = ()
    pass


class ClassInfo:
    Category = ()

    ClassId = ()

    Name = ()

    SuperClassId = ()

    thisown = ()

    def GetCategory(self):
        pass

    def GetClassId(self):
        pass

    def GetName(self):
        pass

    def GetSuperClassId(self):
        pass


class ClassList:
    Classes = ()

    NumClasses = ()

    thisown = ()

    def GetClassInfo(self):
        pass

    def GetNumClasses(self):
        pass



class Color(Wrapper):
    this = ()
    color_spline = ()
    to_COLORREF = ()

    def Black(self):
        pass

    def ClampMax(self):
        pass

    def ClampMin(self):
        pass

    def ClampMinMax(self):
        pass

    def color_spline(self,x,nknots,Color):
        pass

    def GetB(self):
        pass

    def GetG(self):
        pass

    def GetIntensity(self):
        pass

    def GetR(self):
        pass

    def SetB(self,float):
        pass

    def SetG(self,float):
        pass

    def SetR(self,float):
        pass

    def to_COLORREF(self):
        return COLORREF()

    def ToRGB(self):
        return DWORD()

    def White(self):
        pass


class Color64(Wrapper):
    this = ()

    def GetA(self):
        pass

    def GetB(self):
        pass

    def GetG(self):
        pass

    def GetR(self):
        pass

    def SetA(self):
        pass

    def SetB(self):
        pass

    def SetG(self):
        pass

    def SetR(self):
        pass


class ColorList:
    this = ()
    thisown = ()

    def Append(self):
        pass

    def Delete(self):
        pass

    def GetCount(self):
        pass

    def GetItem(self):
        pass

    def Insert(self):
        pass

    def SetCount(self):
        pass

    def SetItem(self):
        pass


class Colors:
    Color12fieldGrid = 0

    ColorActiveAxis = 0

    ColorAnimButton = 0

    ColorArcball = 0

    ColorArcballHilite = 0

    ColorAtmosApparatus = 0

    ColorBackLines = 0

    ColorBackVerts = 0

    ColorBones = 0

    ColorCameraClip = 0

    ColorCameraCone = 0

    ColorCameraHoriz = 0

    ColorCameraObj = 0

    ColorCrosshairCursor = 0

    ColorDecayRadius = 0

    ColorDummyObj = 0

    ColorEndEffector = 0

    ColorEndEffectorString = 0

    ColorEndRange = 0

    ColorEndRange1 = 0

    ColorFalloff = 0

    ColorFarRange = 0

    ColorFreeze = 0

    ColorGhostAfter = 0

    ColorGhostBefore = 0

    ColorGizmos = 0

    ColorGrid = 0

    ColorGridIntens = 0

    ColorGroupObj = 0

    ColorHiddenlineUnselected = 0

    ColorHotspot = 0

    ColorIkTerminator = 0

    ColorInactiveAxis = 0

    ColorJointLimitSel = 0

    ColorJointLimitUnsel = 0

    ColorLightObj = 0

    ColorLinkLines = 0

    ColorManipulatorActive = 0

    ColorManipulatorContour = 0

    ColorManipulatorScreen = 0

    ColorManipulatorTrail = 0

    ColorManipulatorX = 0

    ColorManipulatorY = 0

    ColorManipulatorZ = 0

    ColorNearRange = 0

    ColorNurbsCp = 0

    ColorNurbsCv = 0

    ColorNurbsDep = 0

    ColorNurbsError = 0

    ColorNurbsFp = 0

    ColorNurbsFuse = 0

    ColorNurbsHilite = 0

    ColorNurbsLattice = 0

    ColorParticleEm = 0

    ColorPatchLattice = 0

    ColorPointAxes = 0

    ColorPointObj = 0

    ColorSelBoxes = 0

    ColorSelection = 0

    ColorSelGizmos = 0

    ColorSetkeyButton = 0

    ColorSfAction = 0

    ColorSfLive = 0

    ColorSfTitle = 0

    ColorSfUser = 0

    ColorSnapAxisCenterHandle = 0

    ColorSnapPointActive = 0

    ColorSnapPointSnapped = 0

    ColorSpaceWarps = 0

    ColorSplineHandles = 0

    ColorSplineKnotFirst = 0

    ColorSplineKnotUnselected = 0

    ColorSplineVecs = 0

    ColorStartRange = 0

    ColorStartRange1 = 0

    ColorSubselection = 0

    ColorSubselectionHard = 0

    ColorSubselectionMedium = 0

    ColorSubselectionSoft = 0

    ColorSvBaseobjectBk = 0

    ColorSvCameraBk = 0

    ColorSvChildLine = 0

    ColorSvControllerBk = 0

    ColorSvFrame = 0

    ColorSvGeomobjectBk = 0

    ColorSvGrid = 0

    ColorSvHelperBk = 0

    ColorSvLightBk = 0

    ColorSvMapBk = 0

    ColorSvMaterialBk = 0

    ColorSvMaterialHighlight = 0

    ColorSvModifierBk = 0

    ColorSvModifierHighlight = 0

    ColorSvNodebk = 0

    ColorSvNodeHighlight = 0

    ColorSvPluginHighlight = 0

    ColorSvRelConstraint = 0

    ColorSvRelController = 0

    ColorSvRelInstance = 0

    ColorSvRelLight = 0

    ColorSvRelModifier = 0

    ColorSvRelOther = 0

    ColorSvRelParamwire = 0

    ColorSvSelnodebk = 0

    ColorSvSeltext = 0

    ColorSvShapeBk = 0

    ColorSvSpacewarpBk = 0

    ColorSvSubanimLine = 0

    ColorSvSystemBk = 0

    ColorSvText = 0

    ColorSvUnfoldButton = 0

    ColorSvWinbk = 0

    ColorTapeObj = 0

    ColorTargetLine = 0

    ColorTotal = 0

    ColorTrajectory = 0

    ColorTrajTics1 = 0

    ColorTrajTics2 = 0

    ColorTrajTics3 = 0

    ColorUnselTab = 0

    ColorVertNumbers = 0

    ColorVertTicks = 0

    ColorViewportBkg = 0

    ColorVpInactive = 0

    ColorVpLabelHighlight = 0

    ColorVpLabels = 0

    ColorVpStatistics = 0

    ColorVptClipping = 0

    ColorXray = 0



class CommandPanel:
    GetCurEditObject = ()

    GetIsOpen = ()

    IsEditing = ()

    ResumeEditing = ()

    ResumeMotionEditing = ()

    SetCurrentEditObject = ()

    SetOpen = ()

    SuspendEditing = ()

    SuspendMotionEditing = ()

    thisown = ()

    def GetCurEditObject(self):
        pass

    def GetIsOpen(self):
        pass

    def IsEditing(self):
        pass

    def ResumeEditing(self):
        pass

    def ResumeMotionEditing(self):
        pass

    def SetCurrentEditObject(self):
        pass

    def SetOpen(self):
        pass

    def SuspendEditing(self):
        pass

    def SuspendMotionEditing(self):
        pass


class Constants:
    AAtmosDisabled = 0
    AAtmosObjectxref = 0
    AAtmosScenexref = 0
    ABeingAutoDeleted = 0
    AccAll = 0
    AccPrivate = 0
    AccPublic = 0
    AcDirLrCross = 0
    AcDirRlCross = 0
    AChangeParentsDone = 0
    AComponentLocked = 0
    ACtrlDisabled = 0
    AdaptiveCheckBox = 0
    AdaptiveThreshold = 0
    AddkeyFlagged = 0
    AddkeyInterp = 0
    AddkeySelect = 0
    AddWorldLink = 0
    ADependencyTest = 0
    ADependentsBeingEnumerated = 0
    ADerivedobjDontdelete = 0
    AdjtanBreak = 0
    AdjtanLock = 0
    AdvancedDlgButton = 0
    AEvaluating = 0
    AHeld = 0
    AInodeIkPosPinned = 0
    AInodeIkRotPinned = 0
    AInodeIkTerminator = 0
    AInodeInUpdate = 0
    AInodeInUpdateTm = 0
    AIsDeleted = 0
    AllChannels = 0
    AllTrackViews = 0
    ALockTarget = 0
    AlphaFile = 0
    AlphaNone = 0
    AlphaRgb = 0
    AModappDisabled = 0
    AModappDisplayActive = 0
    AModappDynamicBox = 0
    AModappRendering = 0
    AModappSelected = 0
    AModBeingEdited = 0
    AModDisabled = 0
    AModDisabledInrender = 0
    AModDisabledInviews = 0
    AModUseSel = 0
    AnimationCommand = 0
    AnimEnumAbort = 0
    AnimEnumProceed = 0
    AnimEnumSkip = 0
    AnimEnumSkipNode = 0
    AnimEnumStop = 0
    AnimlayermgrComboboxId = 0
    AnimlayermgrEditId = 0
    AnimlayermgrSpinnerId = 0
    AnimtypeControl = 0
    AnimtypeNode = 0
    AnimtypeRootnode = 0
    ANotifydep = 0
    AObjBeingEdited = 0
    AObjCreating = 0
    AObjectReduced = 0
    AoClosedialog = 0
    AoDefault = 0
    AOrtAftershift = 0
    AOrtBeforeshift = 0
    AOrtDisabled = 0
    AOrtMask = 0
    APlugin1 = 0
    APlugin2 = 0
    APlugin3 = 0
    APlugin4 = 0
    AppCatalogsDir = 0
    AppCuiDir = 0
    AppCuiScriptsDir = 0
    AppCuiWriteDir = 0
    AppendrollClosed = 0
    AppFilelinkDir = 0
    AppFoliageDir = 0
    AppFxDir = 0
    AppIntOffset = 0
    AppLastSpecDir = 0
    AppMapDir = 0
    AppMarketDefWriteDir = 0
    AppPluginIniDir = 0
    AppPluginsDir = 0
    AppStdplugsDir = 0
    AppXrefDir = 0
    ArcFrom = 0
    ArcPie = 0
    ArcRadius = 0
    ArcReverse = 0
    ArcTo = 0
    ARefmakerRefsChecked = 0
    AReservedB16 = 0
    ASet = 0
    ASuperclass1 = 0
    ASuperclass2 = 0
    AToneopDisabled = 0
    AToneopIndirectOnly = 0
    AToneopProcessBg = 0
    AttachmatIdtomat = 0
    AttachmatMattoid = 0
    AttachmatNeither = 0
    Atten1End = 0
    Atten1Start = 0
    AttenEnd = 0
    AttenStart = 0
    AttribAlledges = 0
    AttribBackcull = 0
    AttribBoxmode = 0
    AttribCastshadows = 0
    AttribCverts = 0
    AttribEdgeA = 0
    AttribEdgeAll = 0
    AttribEdgeB = 0
    AttribEdgeC = 0
    AttribFreeze = 0
    AttribFreezeUnsel = 0
    AttribFreezeWithLayer = 0
    AttribFrzmtl = 0
    AttribGeneratecaustics = 0
    AttribGenerateglobalillum = 0
    AttribHide = 0
    AttribHideFace = 0
    AttribHideUnsel = 0
    AttribHideWithLayer = 0
    AttribIgnoreExt = 0
    AttribInheritvisibility = 0
    AttribIstarget = 0
    AttribLinkdisp = 0
    AttribLinkrepl = 0
    AttribMatid = 0
    AttribMatidMask = 0
    AttribMatidShift = 0
    AttribMotionblur = 0
    AttribPrimaryvisibility = 0
    AttribRcvcaustics = 0
    AttribRcvglobalillum = 0
    AttribReceiveshadows = 0
    AttribRenderable = 0
    AttribRenderoccluded = 0
    AttribSecondaryvisibility = 0
    AttribSetgbufid = 0
    AttribSetwirecolor = 0
    AttribShadeCverts = 0
    AttribTrajectory = 0
    AttribUnfreeze = 0
    AttribUnhide = 0
    AttribUnsel = 0
    AttribVertticks = 0
    AttribXray = 0
    ATvnodeDontresaclecontrollers = 0
    AWork1 = 0
    AWork2 = 0
    AWork3 = 0
    AWork4 = 0
    AxisUv = 0
    AxisVw = 0
    AxisWu = 0
    AxisX = 0
    AxisXy = 0
    AxisY = 0
    AxisYz = 0
    AxisZ = 0
    AxisZx = 0
    BadMacroId = 0
    BeginEditCreate = 0
    BeginEditHierarchy = 0
    BeginEditIk = 0
    BeginEditLinkinfo = 0
    BeginEditMotion = 0
    BeginEditShapeNoRendparam = 0
    BendAngle = 0
    BendAxis = 0
    BendDir = 0
    BendDoregion = 0
    BendFrom = 0
    BendTo = 0
    BezfontOther = 0
    BezfontTruetype = 0
    BezkeyConstvelocity = 0
    BezkeyFast = 0
    BezkeyFlat = 0
    BezkeyIntypeshift = 0
    BezkeyLinear = 0
    BezkeyNumtypebits = 0
    BezkeyOuttypeshift = 0
    BezkeySlow = 0
    BezkeySmooth = 0
    BezkeyStep = 0
    BezkeyTypemask = 0
    BezkeyUnconstrainhandle = 0
    BezkeyUser = 0
    BezkeyWbroken = 0
    BezkeyXbroken = 0
    BezkeyYbroken = 0
    BezkeyZbroken = 0
    BezShapeInterpolated = 0
    BezShapeKnot = 0
    BigmatMaxSize = 0
    BitmapDroptype = 0
    BmmAssetGroup = 0
    BmmAssetProxy = 0
    BmmBmp4 = 0
    BmmChanBg = 0
    BmmChanColor = 0
    BmmChanCoverage = 0
    BmmChanMask = 0
    BmmChanMtlId = 0
    BmmChannelAlpha = 0
    BmmChannelBlue = 0
    BmmChannelGreen = 0
    BmmChannelLuminance = 0
    BmmChannelRed = 0
    BmmChannelZ = 0
    BmmChanNodeId = 0
    BmmChanNodeRenderId = 0
    BmmChanNone = 0
    BmmChanNormal = 0
    BmmChanRealpix = 0
    BmmChanTransp = 0
    BmmChanType16 = 0
    BmmChanType24 = 0
    BmmChanType32 = 0
    BmmChanType48 = 0
    BmmChanType64 = 0
    BmmChanType8 = 0
    BmmChanType96 = 0
    BmmChanTypeUnknown = 0
    BmmChanUv = 0
    BmmChanVeloc = 0
    BmmChanWeight = 0
    BmmChanZ = 0
    BmmCheckabort = 0
    BmmCloseAbandon = 0
    BmmCloseComplete = 0
    BmmCn = 0
    BmmCustomFilegamma = 0
    BmmCustomGamma = 0
    BmmCustomHdrType = 0
    BmmCustomIflenumfiles = 0
    BmmCustomPos = 0
    BmmCustomPoscn = 0
    BmmCustomPose = 0
    BmmCustomPosn = 0
    BmmCustomPosne = 0
    BmmCustomPosnw = 0
    BmmCustomPoss = 0
    BmmCustomPosse = 0
    BmmCustomPossw = 0
    BmmCustomPosw = 0
    BmmCustomResfit = 0
    BmmCustomSize = 0
    BmmDitherFloyd = 0
    BmmDitherNone = 0
    BmmDoSaveRegion = 0
    BmmEnableSaveRegion = 0
    BmmFilterBuildFailed = 0
    BmmFilterDummy = 0
    BmmFilterLerpWrap = 0
    BmmFilterNoFlags = 0
    BmmFilterNone = 0
    BmmFilterPyramid = 0
    BmmFilterSum = 0
    BmmFloatA32 = 0
    BmmFloatGray32 = 0
    BmmFloatRgb32 = 0
    BmmFloatRgba32 = 0
    BmmFlushRelativeFileResolutionCache = 0
    BmmGetFileInputSequenceFlag = 0
    BmmGray16 = 0
    BmmGray8 = 0
    BmmioControlgeneric = 0
    BmmioControlread = 0
    BmmioControlwrite = 0
    BmmioEvalmatch = 0
    BmmioExtension = 0
    BmmioFramebuffer = 0
    BmmioGrabber = 0
    BmmioIfl = 0
    BmmioInfodlg = 0
    BmmioMultiframe = 0
    BmmioNonConcurrentAccess = 0
    BmmioNone = 0
    BmmioOwnViewer = 0
    BmmioRandomAccess = 0
    BmmioReader = 0
    BmmioThreaded = 0
    BmmioUninterruptible = 0
    BmmioWriter = 0
    BmmLineArt = 0
    BmmLl = 0
    BmmLogluv24 = 0
    BmmLogluv24a = 0
    BmmLogluv32 = 0
    BmmLr = 0
    BmmNotOpen = 0
    BmmNoType = 0
    BmmOpenR = 0
    BmmOpenW = 0
    BmmPad24 = 0
    BmmPaletted = 0
    BmmProgress = 0
    BmmRealpix32 = 0
    BmmresBadfileheader = 0
    BmmresBadframe = 0
    BmmresCantstorage = 0
    BmmresCorruptfile = 0
    BmmresErrortakencare = 0
    BmmresFilenotfound = 0
    BmmresInternalerror = 0
    BmmresInvalidformat = 0
    BmmresInvalidusage = 0
    BmmresIoerror = 0
    BmmresMemoryerror = 0
    BmmresNodriver = 0
    BmmresNumberedfilenameerror = 0
    BmmresRetry = 0
    BmmresSingleframe = 0
    BmmresSuccess = 0
    BmmRetrieveGeorefData = 0
    BmmRnd = 0
    BmmSeqError = 0
    BmmSeqHold = 0
    BmmSeqWrap = 0
    BmmSetFileInputSequenceFlag = 0
    BmmStoreGeorefData = 0
    BmmTextmsg = 0
    BmmTrue16 = 0
    BmmTrue24 = 0
    BmmTrue32 = 0
    BmmTrue48 = 0
    BmmTrue64 = 0
    BmmUl = 0
    BmmUndefFrame = 0
    BmmUr = 0
    BmmUseCustomFilterlist = 0
    BmmVpp = 0
    BmmVps = 0
    BmmYuv422 = 0
    BmnotifyFlagFileChange = 0
    BmnotifyFlagStorageChange = 0
    BnButtondown = 0
    BnButtonup = 0
    BnFlyoff = 0
    BnRightclick = 0
    BombChaos = 0
    BombDetonation = 0
    BombGravity = 0
    BombStrength = 0
    BoneAbsoluteFlag = 0
    BoneAxisX = 0
    BoneAxisY = 0
    BoneAxisZ = 0
    BoneBoneFlag = 0
    BoneDeadFlag = 0
    BoneDrawEnvelopeFlag = 0
    BoneLockFlag = 0
    BoneScaletypeNone = 0
    BoneScaletypeScale = 0
    BoneScaletypeSquash = 0
    BoneSplineclosedFlag = 0
    BoneSplineFlag = 0
    BoolAddopCopy = 0
    BoolAddopInstance = 0
    BoolAddopMove = 0
    BoolAddopReference = 0
    BoolIntersection = 0
    BoolMatDiscardNew = 0
    BoolMatDiscardOrig = 0
    BoolMatIdtomat = 0
    BoolMatMattoid = 0
    BoolMatNoModify = 0
    BoolopCut = 0
    BoolopCutRefine = 0
    BoolopCutRemoveIn = 0
    BoolopCutRemoveOut = 0
    BoolopCutSeparate = 0
    BoolopIntersection = 0
    BoolopSubAb = 0
    BoolopSubBa = 0
    BoolopUnion = 0
    BoolPblockRef = 0
    BoolrefCont1 = 0
    BoolrefCont2 = 0
    BoolrefObject1 = 0
    BoolrefObject2 = 0
    BoolrefPblock = 0
    BoolSubtraction = 0
    BoolUnion = 0
    BoolupdateAlways = 0
    BoolupdateManual = 0
    BoolupdateRender = 0
    BoolupdateSelected = 0
    BoxCollision = 0
    BoxobjGenuvs = 0
    BoxobjHeight = 0
    BoxobjHsegs = 0
    BoxobjLength = 0
    BoxobjLsegs = 0
    BoxobjWidth = 0
    BoxobjWsegs = 0
    BrowseExistingOnly = 0
    BrowseIncnone = 0
    BrowseInstanceonly = 0
    BrowseMapsonly = 0
    BrowseMatsonly = 0
    BrowseToMeditSlot = 0
    BufFBuffer = 0
    BufferHolding = 0
    BufZBuffer = 0
    BumpChannel = 0
    CameraCommand = 0
    CamHitherClip = 0
    CamYonClip = 0
    Cap3dsOptClosestBridge = 0
    CapfaceAb = 0
    CapfaceBc = 0
    CapfaceCa = 0
    CaptypeGrid = 0
    CaptypeMorph = 0
    CapvertVisedge = 0
    CcCmdHiliteColor = 0
    CcCmdSetState = 0
    CcCmdSetType = 0
    CcColorButtondown = 0
    CcColorButtonup = 0
    CcColorChange = 0
    CcColorClose = 0
    CcColorDrop = 0
    CcColorSel = 0
    CcCommand = 0
    CcSliderButtondown = 0
    CcSliderButtonup = 0
    CcSliderChange = 0
    CcSpinnerButtondown = 0
    CcSpinnerButtonup = 0
    CcSpinnerChange = 0
    CenterToolVertically = 0
    CfAbline = 0
    CfBcline = 0
    CfCaline = 0
    CidAssemblyAttach = 0
    CidBindwsm = 0
    CidBoolean = 0
    CidCamdolly = 0
    CidCamfov = 0
    CidCampersp = 0
    CidCamroll = 0
    CidCamrotate = 0
    CidCamtruck = 0
    CidChamfer = 0
    CidCopyTangent = 0
    CidCopytangent = 0
    CidCreateline = 0
    CidCreatePatch = 0
    CidCreateVert = 0
    CidCrossinsert = 0
    CidCrosssection = 0
    CidEditsoftselection = 0
    CidEpBevel = 0
    CidEpBind = 0
    CidEpExtrude = 0
    CidEpNormalFlip = 0
    CidExtend = 0
    CidFillet = 0
    CidGrpAttach = 0
    CidLink = 0
    CidManipulate = 0
    CidModifyparam = 0
    CidNull = 0
    CidObjmove = 0
    CidObjplace = 0
    CidObjrotate = 0
    CidObjscale = 0
    CidObjselect = 0
    CidObjsquash = 0
    CidObjuscale = 0
    CidOutline = 0
    CidPanview = 0
    CidPasteTangent = 0
    CidPastetangent = 0
    CidPickaxisobject = 0
    CidPlayanimation = 0
    CidRefineconnect = 0
    CidRndregion = 0
    CidRotateview = 0
    CidScreenSpaceRotate = 0
    CidSegbreak = 0
    CidSegrefine = 0
    CidSimplecreate = 0
    CidSplinebind = 0
    CidStdpick = 0
    CidSubobjmove = 0
    CidSubobjrotate = 0
    CidSubobjscale = 0
    CidSubobjselect = 0
    CidSubobjsquash = 0
    CidSubobjuscale = 0
    CidTrim = 0
    CidUnfreeze = 0
    CidUnhide = 0
    CidUser = 0
    CidVertconnect = 0
    CidVertinsert = 0
    CidVertWeld = 0
    CidZoomall = 0
    CidZoomregion = 0
    CidZoomview = 0
    CircleLight = 0
    CircleRadius = 0
    CircleRgn = 0
    ClickDownPoint = 0
    ClickDragClick = 0
    ClickModeDefault = 0
    ClickMoveClick = 0
    ClickStackSize = 0
    ClipEdge = 0
    ClipFace = 0
    ClipPEdge = 0
    ClipPHandle = 0
    ClipPPatch = 0
    ClipPVert = 0
    ClipVert = 0
    ClrChannel = 0
    CmfToolbutton = 0
    CompAll = 0
    CompIgnRect = 0
    CompLighting = 0
    CompObjfrozen = 0
    CompObjselected = 0
    CompTransform = 0
    ConeCapsegments = 0
    ConeGenuvs = 0
    ConeHeight = 0
    ConePieslice1 = 0
    ConePieslice2 = 0
    ConeRadius1 = 0
    ConeRadius2 = 0
    ConeSegments = 0
    ConeSides = 0
    ConeSliceon = 0
    ConeSmooth = 0
    ContDisabledChunk = 0
    ContFlagsChunk = 0
    ControlAspect = 0
    ControlbaseChunk = 0
    ControlCenter = 0
    ControlFit = 0
    ControlHold = 0
    ControlInit = 0
    ControlInitparams = 0
    ControlOp = 0
    ControlUniform = 0
    ConvertKeepsel = 0
    ConvertNoRelax = 0
    ConvertPatchUsequads = 0
    ConvertSelLevel = 0
    ConvertUsesoftsel = 0
    CoordsGimbal = 0
    CoordsHybrid = 0
    CoordsLocal = 0
    CoordsObject = 0
    CoordsParent = 0
    CoordsScreen = 0
    CoordsWorkingpivot = 0
    CoordsWorld = 0
    CopyImageCrop = 0
    CopyImageResizeHiQuality = 0
    CopyImageResizeLoQuality = 0
    CopyImageUseCustom = 0
    CopykeyPos = 0
    CopykeyRot = 0
    CopykeyScale = 0
    CopypasteIkpos = 0
    CopypasteIkrot = 0
    CreateAbort = 0
    CreateCommand = 0
    CreateContinue = 0
    CreateStop = 0
    CuiAllDock = 0
    CuiAllPanels = 0
    CuiBottomDock = 0
    CuiConnectable = 0
    CuiDontSave = 0
    CuiEditKbd = 0
    CuiEditMacro = 0
    CuiEditNone = 0
    CuiEditOrder = 0
    CuiEditScript = 0
    CuiFixedPanels = 0
    CuiFloatable = 0
    CuiFloating = 0
    CuiFloatingPanels = 0
    CuiHasMenubar = 0
    CuiHorizDock = 0
    CuiHwnd = 0
    CuiLeftDock = 0
    CuiMaskAlpha = 0
    CuiMaskAlphaPremult = 0
    CuiMaskMono = 0
    CuiMaskNone = 0
    CuiMaxSize = 0
    CuiMaxSized = 0
    CuiMenu = 0
    CuiMenuHide = 0
    CuiMenuShowDisabled = 0
    CuiMenuShowEnabled = 0
    CuiMinimizedDock = 0
    CuiMinimizedDockable = 0
    CuiMinSize = 0
    CuiMinTbWidth = 0
    CuiModeEdit = 0
    CuiModeNormal = 0
    CuiNone = 0
    CuiNoPanel = 0
    CuiPosdataMsg = 0
    CuiPrefSize = 0
    CuiPresetMacrobuttons = 0
    CuiRightDock = 0
    CuiSize16 = 0
    CuiSize24 = 0
    CuiSliding = 0
    CuiSmHandles = 0
    CuiSubframeActivateMsg = 0
    CuiSubframeAddedMsg = 0
    CuiSubframeRemovedMsg = 0
    CuiToolbar = 0
    CuiTopDock = 0
    CuiVertDock = 0
    CurveCurve = 0
    CurveExtrapolateConstant = 0
    CurveExtrapolateLinear = 0
    CurveLine = 0
    CurvepBezier = 0
    CurvepCorner = 0
    CurvepEndpoint = 0
    CurvepLockedX = 0
    CurvepLockedY = 0
    CurvepNoXConstraint = 0
    CurvepSelected = 0
    CustlistDblSerparator = 0
    CustlistDisabled = 0
    CustlistMedDisabled = 0
    CustlistRed = 0
    CustlistSeparator = 0
    CylinderCapsegments = 0
    CylinderGenuvs = 0
    CylinderHeight = 0
    CylinderPieslice1 = 0
    CylinderPieslice2 = 0
    CylinderRadius = 0
    CylinderSegments = 0
    CylinderSides = 0
    CylinderSliceon = 0
    CylinderSmooth = 0
    DecayInv = 0
    DecayInvsq = 0
    DecayNone = 0
    DefAdaptive = 0
    DefaultactionsAbort = 0
    DefaultactionsDefaultMsgLogMaxsize = 0
    DefaultactionsLogmsg = 0
    DefaultactionsLogtofile = 0
    DefaultBakeChannel = 0
    DefaultNDilations = 0
    DefDisprendermesh = 0
    DefGenuvs = 0
    DeflectorBounce = 0
    DeflectorHeight = 0
    DeflectorWidth = 0
    DefOptimize = 0
    DefPickboxSize = 0
    DefPmBoundary = 0
    DefPmIter = 0
    DefPmRelax = 0
    DefPmRelaxViewports = 0
    DefPmSaddle = 0
    DefRenderable = 0
    DefRenderableSides = 0
    DefSteps = 0
    DepEnumContinue = 0
    DepEnumHalt = 0
    DepEnumSkip = 0
    DfMgrport = 0
    DirLight = 0
    DispApproxChannel = 0
    DispApproxChanNum = 0
    DispAtshapelevel = 0
    DispAttribChannel = 0
    DispAttribChanNum = 0
    DispBezhandles = 0
    DispChannel = 0
    DisplaceApplymap = 0
    DisplaceAxis = 0
    DisplaceBlur = 0
    DisplaceCap = 0
    DisplaceCenterl = 0
    DisplaceCenterlum = 0
    DisplaceDecay = 0
    DisplaceHeight = 0
    DisplaceLength = 0
    DisplaceMaptype = 0
    DisplaceStrength = 0
    DisplaceUflip = 0
    DisplaceUsemap = 0
    DisplaceUtile = 0
    DisplaceVflip = 0
    DisplaceVtile = 0
    DisplaceWflip = 0
    DisplaceWidth = 0
    DisplaceWtile = 0
    DispLattice = 0
    DisplayCommand = 0
    DisplayDialog = 0
    DisplayRubberBand = 0
    DisplaySelectedOnly = 0
    DisplayShadedAsMtl = 0
    DisplayTangentsAll = 0
    DisplayTangentsNone = 0
    DisplayTangentsSelected = 0
    DisplayWcurve = 0
    DisplayWireAsMtl = 0
    DisplayXcurve = 0
    DisplayYcurve = 0
    DisplayZcurve = 0
    DispObjselected = 0
    DispSelected = 0
    DispSeledges = 0
    DispSelfaces = 0
    DispSelhandles = 0
    DispSelpatches = 0
    DispSelpolys = 0
    DispSelsegments = 0
    DispSelverts = 0
    DispShowsubobject = 0
    DispSplinesOrthog = 0
    DispUnselected = 0
    DispVertNumbers = 0
    DispVertNumbersSelonly = 0
    DispVerts = 0
    DispVertticks = 0
    Dontautoclose = 0
    DontRecreateTristripChannel = 0
    DonutRadius1 = 0
    DonutRadius2 = 0
    DownloaddlgNoplace = 0
    DrawDraggingVector = 0
    DrawFreemovePoint = 0
    DrawFreemovePointMouseDown = 0
    DrawIdle = 0
    DrawInitialBezAdj = 0
    DrawInitialMouseDown = 0
    DropscriptDroptype = 0
    DropscriptfileDroptype = 0
    EdataCrease = 0
    EdataKnot = 0
    EdgeA = 0
    EdgeAll = 0
    EdgeB = 0
    EdgeC = 0
    EdgeCollision = 0
    EdgeInvis = 0
    EdgeVis = 0
    EdgevisiblityChannel = 0
    EditBoxItem = 0
    EditrangeLinktokeys = 0
    EdittrackButton = 0
    EdittrackFcurve = 0
    EdittrackMouse = 0
    EdittrackScene = 0
    EdittrackTrack = 0
    EffectAllKeys = 0
    EffectAllKeysInSelTracks = 0
    EffectAllSelKeys = 0
    EffectSelKeysInSelTracks = 0
    EliminateChannel = 0
    EllipseLength = 0
    EllipseWidth = 0
    EmShortcutId = 0
    EmSlEdge = 0
    EmSlElement = 0
    EmSlFace = 0
    EmSlObject = 0
    EmSlPolygon = 0
    EmSlVertex = 0
    EndEditRemoveui = 0
    EndHold = 0
    EndLoop = 0
    EndPingpong = 0
    EnvFarRange = 0
    EnvNearRange = 0
    EpDispResult = 0
    EpMasterControlRef = 0
    EpVertBaseRef = 0
    EsAddedSelect = 0
    EsDispResult = 0
    EsVertBaseRef = 0
    EulertypeRf = 0
    EulertypeXyx = 0
    EulertypeXyz = 0
    EulertypeXzy = 0
    EulertypeYxz = 0
    EulertypeYzx = 0
    EulertypeYzy = 0
    EulertypeZxy = 0
    EulertypeZxz = 0
    EulertypeZyx = 0
    ExAlphaFromRgb = 0
    ExitListener = 0
    ExMultAlpha = 0
    ExOpaqueAlpha = 0
    ExposeWorldTransformSclassId = 0
    ExRgbFromAlpha = 0
    ExtDispDragging = 0
    ExtDispGroupExt = 0
    ExtDispLookatSelected = 0
    ExtDispNone = 0
    ExtDispOnlySelected = 0
    ExtDispSelected = 0
    ExtDispTargetSelected = 0
    ExtDispZoomExt = 0
    ExtDispZoomselExt = 0
    ExtensionChannel = 0
    ExtensionChanNum = 0
    ExtentsFitinrange = 0
    ExtentsSelectedKeys = 0
    ExtentsShowalltangents = 0
    ExtentsShowtangents = 0
    ExtrudeAmount = 0
    ExtrudeCapend = 0
    ExtrudeCapstart = 0
    ExtrudeCaptype = 0
    ExtrudeGenMatids = 0
    ExtrudeMapping = 0
    ExtrudeOutput = 0
    ExtrudeSegs = 0
    ExtrudeSmooth = 0
    ExtrudeUseShapeids = 0
    FaceBackfacing = 0
    FaceHidden = 0
    FaceInforeground = 0
    FaceMatidMask = 0
    FaceMatidShift = 0
    FaceNormA = 0
    FaceNormB = 0
    FaceNormC = 0
    FaceNormMask = 0
    FaceStrip = 0
    FaceWork = 0
    FalloffBottom = 0
    FalloffNone = 0
    FalloffTop = 0
    FenceRgn = 0
    FieldEven = 0
    FieldFirst = 0
    FieldNone = 0
    FieldOdd = 0
    FieldSecond = 0
    FileDroptype = 0
    FileEnum1stsubMissing = 0
    FileEnumAccessorInterface = 0
    FileEnumAll = 0
    FileEnumCheckAwork1 = 0
    FileEnumDontcheckCustattr = 0
    FileEnumDontRecurse = 0
    FileEnumFileSave = 0
    FileEnumInactive = 0
    FileEnumMissingActive = 0
    FileEnumMissingActive1 = 0
    FileEnumMissingOnly = 0
    FileEnumRender = 0
    FileEnumReserved1 = 0
    FileEnumSkipVprenderOnly = 0
    FileEnumVp = 0
    FileFormatChr = 0
    FileFormatRps = 0
    FileProcessAutobak = 0
    FileProcessHoldFetch = 0
    FileProcessScene = 0
    FileSupportDefault = 0
    FileSupportExport = 0
    FileSupportImport = 0
    FileSupportMerge = 0
    FileSupportNone = 0
    FileSupportOpen = 0
    FileSupportReplace = 0
    FileSupportRpsOpen = 0
    FileSupportRpsSave = 0
    FileSupportSave = 0
    FileSupportXref = 0
    FillModeBdiagonal = 0
    FillModeCross = 0
    FillModeDiagcross = 0
    FillModeFdiagonal = 0
    FillModeHorizonal = 0
    FillModeOff = 0
    FillModeSolid = 0
    FillModeVertical = 0
    FilterActivelayer = 0
    FilterAlpha = 0
    FilterAnim = 0
    FilterAnimchannels = 0
    FilterBaseparams = 0
    FilterBlue = 0
    FilterBones = 0
    FilterCameras = 0
    FilterConttypes = 0
    FilterContw = 0
    FilterContx = 0
    FilterConty = 0
    FilterContz = 0
    FilterGeom = 0
    FilterGlobaltracks = 0
    FilterGreen = 0
    FilterHelpers = 0
    FilterHierarchy = 0
    FilterkernelbaseChunk = 0
    FilterkernelnameChunk = 0
    FilterKeyable = 0
    FilterLights = 0
    FilterLocked = 0
    FilterMatmaps = 0
    FilterMatparams = 0
    FilterNada = 0
    FilterNode = 0
    FilterNodes = 0
    FilterNone = 0
    FilterNotetracks = 0
    FilterObjectmods = 0
    FilterPosition = 0
    FilterPosw = 0
    FilterPosx = 0
    FilterPosy = 0
    FilterPosz = 0
    FilterPyr = 0
    FilterRed = 0
    FilterRotation = 0
    FilterRotx = 0
    FilterRoty = 0
    FilterRotz = 0
    FilterSat = 0
    FilterScale = 0
    FilterScalex = 0
    FilterScaley = 0
    FilterScalez = 0
    FilterSelchannels = 0
    FilterSelobjects = 0
    FilterShapes = 0
    FilterSound = 0
    FilterStaticvals = 0
    FilterSubtree = 0
    FilterTransform = 0
    FilterVisibleObjs = 0
    FilterVistracks = 0
    FilterWarps = 0
    FilterWorldmods = 0
    FlagCurvedmapping = 0
    FlagDead = 0
    FlagFrozen = 0
    FlagHidden = 0
    FlagHiddenedgea = 0
    FlagHiddenedgeb = 0
    FlagHiddenedgec = 0
    FlagInterior = 0
    FlagRigpoint = 0
    FlagSelected = 0
    FlagWeightmodified = 0
    FltCheckabort = 0
    FltFilter = 0
    FltLayer = 0
    FltProgress = 0
    FltTextmsg = 0
    FltTimechanged = 0
    FltUndo = 0
    FlyDown = 0
    FlyHvariable = 0
    FlyLeft = 0
    FlyRight = 0
    FlyUp = 0
    FlyVariable = 0
    FpAction = 0
    FpActions = 0
    FpClientOwnsResult = 0
    FpCore = 0
    FpHasKeyargs = 0
    FpHasShortcut = 0
    FpHasUi = 0
    FpIconfile = 0
    FpIconres = 0
    FpMixin = 0
    FpNoRedraw = 0
    FppHasRange = 0
    FppHasValidator = 0
    FppIndex = 0
    FppInOutParam = 0
    FppInParam = 0
    FppKeyarg = 0
    FppOutParam = 0
    FpsActionDisabled = 0
    FpScriptedClass = 0
    FpsFail = 0
    FpsNoSuchFunction = 0
    FpsOk = 0
    FpStaticMethods = 0
    FpTemporary = 0
    FpTestInterface = 0
    FpVarArgs = 0
    FrAll = 0
    FreeCamera = 0
    FrV0 = 0
    FrV1 = 0
    FrV2 = 0
    FspotLight = 0
    GbBg = 0
    GbColor = 0
    GbCoverage = 0
    GbMask = 0
    GbMtlId = 0
    GbNodeId = 0
    GbNodeRenderId = 0
    GbNormal = 0
    GbRealpix = 0
    GbTransp = 0
    GbUv = 0
    GbVeloc = 0
    GbWeight = 0
    GbZ = 0
    GenmeshDefault = 0
    GenmeshRender = 0
    GenmeshViewport = 0
    GeomChannel = 0
    GeomChanNum = 0
    GfxDataChannel = 0
    GfxDataChanNum = 0
    GfxMaxColors = 0
    GfxMaxStrip = 0
    GfxMaxTextures = 0
    Gizmocolor = 0
    GlobmtlChannel = 0
    GravityDecay = 0
    GravityDisplength = 0
    GravityStrength = 0
    GravityType = 0
    GridhelpGrid = 0
    GridhelpLength = 0
    GridhelpWidth = 0
    GridPlaneBack = 0
    GridPlaneBottom = 0
    GridPlaneFront = 0
    GridPlaneLeft = 0
    GridPlaneNone = 0
    GridPlaneRight = 0
    GridPlaneTop = 0
    GupresultAbort = 0
    GupresultKeep = 0
    GupresultNokeep = 0
    GwAllEdges = 0
    GwAllOpaque = 0
    GwAttenEnd = 0
    GwAttenLinear = 0
    GwAttenNone = 0
    GwAttenQuad = 0
    GwAttenStart = 0
    GwBackcull = 0
    GwBackPlane = 0
    GwBlending = 0
    GwBottomPlane = 0
    GwBoxMode = 0
    GwColorVerts = 0
    GwConstant = 0
    GwCustom = 0
    GwDepthwriteDisable = 0
    GwDirect3d = 0
    GwDisplayInvisible = 0
    GwDisplayMaximized = 0
    GwDisplayWindowed = 0
    GwDoesNotSupport = 0
    GwDoesSupport = 0
    GwDrvDevice = 0
    GwDrvRenderer = 0
    GwEdgeInvis = 0
    GwEdgeSkip = 0
    GwEdgesOnly = 0
    GwEdgeVis = 0
    GwEmissiveVerts = 0
    GwFlat = 0
    GwFrontPlane = 0
    GwHeidi = 0
    GwHeidi3d = 0
    GwHiddenline = 0
    GwIllum = 0
    GwLeftPlane = 0
    GwLighting = 0
    GwMaxCaptionLen = 0
    GwMaxFileLen = 0
    GwMaxVerts = 0
    GwNitrous = 0
    GwNoAtts = 0
    GwNull = 0
    GwOpengl = 0
    GwPassOne = 0
    GwPassTwo = 0
    GwPerspCorrect = 0
    GwPick = 0
    GwPlaneMask = 0
    GwPolyEdges = 0
    GwRightPlane = 0
    GwShadeCverts = 0
    GwShadeSelFaces = 0
    GwShapeCircular = 0
    GwShapeRect = 0
    GwSpecular = 0
    GwSpt1PassDecal = 0
    GwSptArrayProcessing = 0
    GwSptDriverConfig = 0
    GwSptDualPlanes = 0
    GwSptGeomAccel = 0
    GwSptIncrUpdate = 0
    GwSptNumLights = 0
    GwSptNumTextures = 0
    GwSptOrgUpperLeft = 0
    GwSptPaintDoesBlit = 0
    GwSptSwapModel = 0
    GwSptTexturedBkg = 0
    GwSptTotal = 0
    GwSptTriStrips = 0
    GwSptTxtCorrect = 0
    GwSptVirtualVpts = 0
    GwSptWireFaces = 0
    GwSptWireframeStrips = 0
    GwTexAdd = 0
    GwTexAddSigned = 0
    GwTexAddSmooth = 0
    GwTexAlphaBlend = 0
    GwTexAlphaBlend2 = 0
    GwTexConstant = 0
    GwTexLeave = 0
    GwTexMirror = 0
    GwTexModulate = 0
    GwTexNoTiling = 0
    GwTexPremultAlphaBlend = 0
    GwTexPrevious = 0
    GwTexRepeat = 0
    GwTexReplace = 0
    GwTexScale1x = 0
    GwTexScale2x = 0
    GwTexScale4x = 0
    GwTexSource = 0
    GwTexSubtract = 0
    GwTexTexture = 0
    GwTexture = 0
    GwTexZero = 0
    GwTopPlane = 0
    GwTransparency = 0
    GwTransparentPass = 0
    GwTwoSided = 0
    GwVertTicks = 0
    GwWireframe = 0
    GwZBuffer = 0
    HandleBox2 = 0
    HandleBox3 = 0
    HandleBox4 = 0
    HandleBox5 = 0
    HandleBox6 = 0
    HandleBox7 = 0
    HasBumps = 0
    HasMatteMtl = 0
    HasOpacity = 0
    HasReflect = 0
    HasReflectMap = 0
    HasRefract = 0
    HasRefractMap = 0
    HedraFamily = 0
    HedraGenuvs = 0
    HedraP = 0
    HedraQ = 0
    HedraRadius = 0
    HedraScalep = 0
    HedraScaleq = 0
    HedraScaler = 0
    HedraVerts = 0
    HelixBias = 0
    HelixDirection = 0
    HelixHeight = 0
    HelixRadius1 = 0
    HelixRadius2 = 0
    HelixTurns = 0
    HideAll = 0
    HideBoneobjects = 0
    HideCameras = 0
    HideHelpers = 0
    HideLights = 0
    HideNone = 0
    HideObjects = 0
    HideParticles = 0
    HideShapes = 0
    HideSystems = 0
    HideWsms = 0
    HierarchyCommand = 0
    HighlightGeom = 0
    HighlightPoint = 0
    HiliteBox = 0
    HiliteCrosshair = 0
    HiliteNode = 0
    HiliteNormal = 0
    HitAbortonhit = 0
    HitAnysolid = 0
    HitcurveAskclient = 0
    HitcurveKey = 0
    HitcurveNone = 0
    HitcurveTangent = 0
    HitcurveTestalltangents = 0
    HitcurveTesttangents = 0
    HitcurveWhole = 0
    HitflagStartuserbit = 0
    HitfltrAll = 0
    HitfltrBones = 0
    HitfltrCameras = 0
    HitfltrHelpers = 0
    HitfltrLights = 0
    HitfltrObjects = 0
    HitfltrSplines = 0
    HitfltrWsmobjects = 0
    HitkeyIntan = 0
    HitkeyOuttan = 0
    HitManagerHiddenScenexrefs = 0
    HitManipSubhit = 0
    HitScenexrefs = 0
    HitSelonly = 0
    HitSelsolid = 0
    HitSwitchGizmo = 0
    HittrackAbortonhit = 0
    HittrackSelonly = 0
    HittrackSubtreemode = 0
    HittrackUnselonly = 0
    HitTransformgizmo = 0
    HittypeBox = 0
    HittypeCircle = 0
    HittypeFence = 0
    HittypeLasso = 0
    HittypePaint = 0
    HittypePoint = 0
    HittypeSolid = 0
    HitUnselonly = 0
    HoldPointerIsManager = 0
    HoldSuperlevel = 0
    HoldSystemEmpty = 0
    HotkeyAll = 0
    HotkeyAllPos = 0
    HotkeyAllPosrotscale = 0
    HotkeyAllPosx = 0
    HotkeyAllPosy = 0
    HotkeyAllPosz = 0
    HotkeyAllRot = 0
    HotkeyAllRotx = 0
    HotkeyAllRoty = 0
    HotkeyAllRotz = 0
    HotkeyAllScale = 0
    HotkeyAllScalex = 0
    HotkeyAllScaley = 0
    HotkeyAllScalez = 0
    IControl = 0
    IconWidth = 0
    IdAm = 0
    IdBu = 0
    IdDi = 0
    IdDp = 0
    IdFi = 0
    IdIrenderAutomaticPreshade = 0
    IdIrenderAutomaticReshade = 0
    IdIrenderPreshade = 0
    IdIrenderReshade = 0
    IdIreshadeActOnlyMouseUp = 0
    IdIreshadeToggleToolbarDocked = 0
    IdOp = 0
    IdPatchMenu = 0
    IdRayReflection = 0
    IdRayRefraction = 0
    IdRayRefractionIor = 0
    IdRl = 0
    IdRr = 0
    IdSh = 0
    IdSi = 0
    IdSp = 0
    IdSplineMenu = 0
    IdSs = 0
    IdToolBreak = 0
    IdToolDecselected = 0
    IdToolFalloff = 0
    IdToolFalloffSpace = 0
    IdToolFilterMatid = 0
    IdToolFilterSelectedfaces = 0
    IdToolFlip = 0
    IdToolFreeze = 0
    IdToolHide = 0
    IdToolIncselected = 0
    IdToolLockselected = 0
    IdToolMirror = 0
    IdToolMove = 0
    IdToolMovepivot = 0
    IdToolPan = 0
    IdToolPickmap = 0
    IdToolProp = 0
    IdToolRotate = 0
    IdToolScale = 0
    IdToolSelect = 0
    IdToolShowmap = 0
    IdToolSnap = 0
    IdToolTextureCombo = 0
    IdToolUnfreeze = 0
    IdToolUnhide = 0
    IdToolUpdate = 0
    IdToolUvw = 0
    IdToolWeld = 0
    IdToolWeldSel = 0
    IdToolZoom = 0
    IdToolZoomext = 0
    IdToolZoomreg = 0
    IdTranslucentClr = 0
    IdTvAdd = 0
    IdTvAddnote = 0
    IdTvAddvis = 0
    IdTvAlignkeys = 0
    IdTvAssigncontrol = 0
    IdTvAutoexpandAnimated = 0
    IdTvAutoexpandKeyable = 0
    IdTvAutoexpandLimits = 0
    IdTvAutoexpandLocked = 0
    IdTvBreakTangents = 0
    IdTvChooseEaseOrt = 0
    IdTvChooseMultOrt = 0
    IdTvChooseort = 0
    IdTvCollapseall = 0
    IdTvCollapsenodes = 0
    IdTvCollapsetracks = 0
    IdTvCopy = 0
    IdTvCopylimitonly = 0
    IdTvCopytrack = 0
    IdTvCut = 0
    IdTvDelease = 0
    IdTvDeletecontrol = 0
    IdTvDeletenote = 0
    IdTvDeletetime = 0
    IdTvDelvis = 0
    IdTvDrawcurves = 0
    IdTvEdittrackset = 0
    IdTvEditTracksets = 0
    IdTvExpandall = 0
    IdTvExpandnodes = 0
    IdTvExpandtracks = 0
    IdTvFilters = 0
    IdTvFilterSelectedtracks = 0
    IdTvFreezenonselcurves = 0
    IdTvFreezesel = 0
    IdTvGetselected = 0
    IdTvHfittowindow = 0
    IdTvHidenonselcurves = 0
    IdTvIgnoreAnimRange = 0
    IdTvInsert = 0
    IdTvIsolateCurve = 0
    IdTvKAccessselname = 0
    IdTvKAccesstime = 0
    IdTvKAccesstname = 0
    IdTvKAccessval = 0
    IdTvKApplyease = 0
    IdTvKApplymult = 0
    IdTvKLeftend = 0
    IdTvKLocktan = 0
    IdTvKMovechilddown = 0
    IdTvKMovechildup = 0
    IdTvKMovehorz = 0
    IdTvKMovekeys = 0
    IdTvKMovevert = 0
    IdTvKRightend = 0
    IdTvKSeltime = 0
    IdTvKShowstat = 0
    IdTvKShowtan = 0
    IdTvKSnap = 0
    IdTvKSubtree = 0
    IdTvKTemplate = 0
    IdTvKZoom = 0
    IdTvKZoomhorz = 0
    IdTvKZoomhorzkeys = 0
    IdTvKZoomtime = 0
    IdTvKZoomvalue = 0
    IdTvLeftend = 0
    IdTvLocktan = 0
    IdTvMakeunique = 0
    IdTvMaximize = 0
    IdTvMove = 0
    IdTvNewease = 0
    IdTvPan = 0
    IdTvPaste = 0
    IdTvPastelimitonly = 0
    IdTvPastetrack = 0
    IdTvProperties = 0
    IdTvRecouplerange = 0
    IdTvReducekeys = 0
    IdTvRegionTool = 0
    IdTvRemovelimit = 0
    IdTvRespectAnimRange = 0
    IdTvReverse = 0
    IdTvRightend = 0
    IdTvScale = 0
    IdTvScaletime = 0
    IdTvScalevalues = 0
    IdTvSelect = 0
    IdTvSelectall = 0
    IdTvSelectchildren = 0
    IdTvSelectinvert = 0
    IdTvSelectnone = 0
    IdTvSelwildcard = 0
    IdTvSetlowerlimit = 0
    IdTvSetupperlimit = 0
    IdTvShowalltangents = 0
    IdTvShowkeysonfrozen = 0
    IdTvShowstats = 0
    IdTvShowtangents = 0
    IdTvSlide = 0
    IdTvSnapkeys = 0
    IdTvStatus = 0
    IdTvSubtree = 0
    IdTvTangentCustom = 0
    IdTvTangentFast = 0
    IdTvTangentFlat = 0
    IdTvTangentLinear = 0
    IdTvTangentSlow = 0
    IdTvTangentSmooth = 0
    IdTvTangentStep = 0
    IdTvTemplate = 0
    IdTvTimetypein = 0
    IdTvToggleease = 0
    IdTvToggleKeyable = 0
    IdTvTogglelimit = 0
    IdTvToggleLocked = 0
    IdTvToolbar = 0
    IdTvTracksetlist = 0
    IdTvTvname = 0
    IdTvTvutil = 0
    IdTvUnifyTangents = 0
    IdTvValuetypein = 0
    IdTvVfittowindow = 0
    IdTvZoom = 0
    IdTvZoomregion = 0
    IdTvZoomsel = 0
    IExecActivateTexture = 0
    IExecButtonDadEnable = 0
    IExecCbNoBorder = 0
    IExecCountMtlScenerefs = 0
    IExecCsNoBorder = 0
    IExecDeactivateTexture = 0
    IExecGetTooltipHwnd = 0
    IExecGetVpdisplayDib = 0
    IExecInvalidateViewexp = 0
    IExecModifytaskInvalidatepanel = 0
    IExecNewObjXrefDlg = 0
    IExecOffsetMeasure = 0
    IExecOffsetSpline = 0
    IExecRegisterPostsaveCb = 0
    IExecRegisterPresaveCb = 0
    IExecRenderMtlSample = 0
    IExecRetNotSpline = 0
    IExecRetNullNode = 0
    IExecRetNullObject = 0
    IExecRetOffsetFail = 0
    IExecSetDir = 0
    IExecSetNudge = 0
    IExecSpinnerAltDisable = 0
    IExecSpinnerAltEnable = 0
    IExecSpinnerIsResetChange = 0
    IExecSpinnerOneClickDisable = 0
    IExecSpinnerOneClickEnable = 0
    IExecSpinnerReset = 0
    IExecTrimExtend = 0
    IExecUnregisterPostsaveCb = 0
    IExecUnregisterPresaveCb = 0
    IGizmo = 0
    IGizmo2 = 0
    IGizmo3 = 0
    IidIindirectreferencemaker = 0
    IidIreshading = 0
    IidIvaliditytoken = 0
    IidRaytraceMap = 0
    IidReftargMonitor = 0
    IkeyAllsel = 0
    IkeyFlagged = 0
    IkeySelected = 0
    IkeyTimeLock = 0
    IkeyValaLock = 0
    IkeyVallockShift = 0
    IkeyValxLock = 0
    IkeyValyLock = 0
    IkeyValzLock = 0
    IkeyWsel = 0
    IkeyXsel = 0
    IkeyYsel = 0
    IkeyZsel = 0
    ILayerInterface = 0
    ImagefileDroptype = 0
    ImbTransp = 0
    ImeshselEdge = 0
    ImeshselFace = 0
    ImeshselObject = 0
    ImeshselVertex = 0
    ImgfltCompositor = 0
    ImgfltControl = 0
    ImgfltFilter = 0
    ImgfltMask = 0
    ImgfltNone = 0
    ImgfltThreaded = 0
    IMixslaveinterface = 0
    ImpexpCancel = 0
    ImpexpFail = 0
    ImpexpSuccess = 0
    ImportfileDroptype = 0
    InCurvetangentChanged = 0
    InheritAll = 0
    InheritPosX = 0
    InheritPosY = 0
    InheritPosZ = 0
    InheritRotX = 0
    InheritRotY = 0
    InheritRotZ = 0
    InheritSclX = 0
    InheritSclY = 0
    InheritSclZ = 0
    INodedisplaycontrol = 0
    InodeLockpos = 0
    InodeLockrot = 0
    InodeLockscl = 0
    InodeLockX = 0
    InodeLockY = 0
    InodeLockZ = 0
    InortChunk = 0
    InstanceMgrMakeUniqueGroup = 0
    InstanceMgrMakeUniqueIndividual = 0
    InstanceMgrMakeUniquePrompt = 0
    InstBlur = 0
    InstClip = 0
    InstHide = 0
    InstMtlByface = 0
    InstRcvShadows = 0
    InstTmNegparity = 0
    IntBits = 0
    InterruptEval = 0
    InvalidHierarchy = 0
    IpbAdaptive = 0
    Ipblock = 0
    IpbOptimize = 0
    IpbSteps = 0
    IResmakerInterface = 0
    IsAdaptive = 0
    ISetkeymode = 0
    ISkin = 0
    ISkin2 = 0
    ISkinimportdata = 0
    IsMesh = 0
    IsMnmesh = 0
    IsNurbs = 0
    IsPatch = 0
    IWavepaint = 0
    JiggleControlRef = 0
    Jigglep3 = 0
    JigglePblockRef1 = 0
    JigglePblockRef2 = 0
    Jigglepos = 0
    JntLimitexact = 0
    JntParams2 = 0
    JntParamsEuler = 0
    JntPos = 0
    JntRollopen = 0
    JntRot = 0
    JntXactive = 0
    JntXease = 0
    JntXlimited = 0
    JntXspring = 0
    JntYactive = 0
    JntYease = 0
    JntYlimited = 0
    JntYspring = 0
    JntZactive = 0
    JntZease = 0
    JntZlimited = 0
    JntZspring = 0
    JobAllservers = 0
    JobAssignRnd = 0
    JobCombustionjob = 0
    JobComplete = 0
    JobDefaultPriority = 0
    JobIgnoreshare = 0
    JobInactive = 0
    JobMaps = 0
    JobNonc = 0
    JobNonseqframes = 0
    JobNonstop = 0
    JobNotarchived = 0
    JobPriorityCritical = 0
    JobRenderCrop = 0
    JobSkipexst = 0
    JobSkipoutputtst = 0
    JobStateBusy = 0
    JobStateComplete = 0
    JobStateError = 0
    JobStateSuspended = 0
    JobStateWaiting = 0
    JobVersion = 0
    JobVfb = 0
    JobVp = 0
    JpHeld = 0
    KeyatPosition = 0
    KeyatRotation = 0
    KeyatScale = 0
    KeycoordsExprError = 0
    KeycoordsExprOk = 0
    KeycoordsExprUnsupported = 0
    KeycoordsTimeonly = 0
    KeycoordsValueonly = 0
    KeyModeNoBuffer = 0
    KeyreduceAbort = 0
    KeyreduceContinue = 0
    KeyreduceStop = 0
    KeysCommontime = 0
    KeysCommonvalue = 0
    KeysMultiselected = 0
    KeysNoneselected = 0
    KtFlagDelayKeyschanged = 0
    KtypeAuto = 0
    KtypeBezier = 0
    KtypeBezierCorner = 0
    KtypeCorner = 0
    KtypeReset = 0
    LargeVertexDots = 0
    LayerDim = 0
    LeftButton = 0
    LgDebug = 0
    LgFatal = 0
    LgInfo = 0
    LgNolog = 0
    LgWarn = 0
    LightAttenEnd = 0
    LightAttenStart = 0
    LightshadowMapped = 0
    LightshadowNone = 0
    LightshadowRaytraced = 0
    LineCurve = 0
    LineLine = 0
    LinkctrlControlRef = 0
    LinkctrlCoreRefs = 0
    LinkctrlFirstparentRef = 0
    LinkctrlLtctlRef = 0
    LinkctrlPblockRef = 0
    ListenerStyleInput = 0
    ListenerStyleLabel = 0
    ListenerStyleMessage = 0
    ListenerStyleOutput = 0
    LookatPosRef = 0
    LookatRollRef = 0
    LookatRotPblockRef = 0
    LookatSclRef = 0
    LookatTargetRef = 0
    LsnrBlockMiniUpdates = 0
    LsnrInputModeMask = 0
    LsnrKeyinputChar = 0
    LsnrKeyinputLine = 0
    LsnrKeyinputOff = 0
    LsnrNoMacroRedraw = 0
    LsnrQuitmaxRun = 0
    LsnrShowing = 0
    LsnrStyleInput = 0
    LsnrStyleMask = 0
    LsnrStyleMessage = 0
    LsnrStyleOutput = 0
    LtypeCurve = 0
    LtypeLine = 0
    MacrorecBoxItem = 0
    ManipulateCommand = 0
    MapAcadBox = 0
    MapAcadCylindrical = 0
    MapAcadPlanar = 0
    MapAcadSpherical = 0
    MapAllFlags = 0
    MapAlpha = 0
    MapAlphaPremultiplied = 0
    MapBall = 0
    MapBox = 0
    MapCylindrical = 0
    MapDithered = 0
    MapFace = 0
    MapFlipped = 0
    MapFrameSystemLocked = 0
    MapHasAlpha = 0
    MapHasBgimage = 0
    MapInverted = 0
    MapLegalDelete = 0
    MapNoFlags = 0
    MapPaletted = 0
    MapPlanar = 0
    MapProxy = 0
    MapProxyrequest = 0
    MapReady = 0
    MapShading = 0
    MapslotBackground = 0
    MapslotDisplacement = 0
    MapslotEnviron = 0
    MapslotTexture = 0
    MapSpherical = 0
    MapUseScaleColors = 0
    MapViewFiltered = 0
    MatIdent = 0
    MatmodMatid = 0
    MaxApiNumR100 = 0
    MaxApiNumR100Beta5 = 0
    MaxApiNumR110 = 0
    MaxApiNumR110Alpha = 0
    MaxApiNumR120 = 0
    MaxApiNumR120Alpha2 = 0
    MaxApiNumR120Alpha3 = 0
    MaxApiNumR120Alpha4 = 0
    MaxApiNumR120Beta1 = 0
    MaxApiNumR120Beta3 = 0
    MaxApiNumR120Beta4 = 0
    MaxApiNumR120Beta5 = 0
    MaxApiNumR130 = 0
    MaxApiNumR130Beta1 = 0
    MaxApiNumR140 = 0
    MaxApiNumR140Alpha1 = 0
    MaxApiNumR140Beta2 = 0
    MaxApiNumR20 = 0
    MaxApiNumR25 = 0
    MaxApiNumR30 = 0
    MaxApiNumR31 = 0
    MaxApiNumR40 = 0
    MaxApiNumR42 = 0
    MaxApiNumR50 = 0
    MaxApiNumR60 = 0
    MaxApiNumR60PreRel = 0
    MaxApiNumR70 = 0
    MaxApiNumR70PreRel = 0
    MaxApiNumR80 = 0
    MaxApiNumR80PreRel = 0
    MaxApiNumR90 = 0
    MaxApiNumR90Alpha = 0
    MaxApiNumR90Beta1 = 0
    MaxApiNumR90Beta3 = 0
    MaxCellLevels = 0
    Maxcolors = 0
    MaxDescription = 0
    MaxEdgedata = 0
    MaxFracTypes = 0
    MaxMbDontshowagain = 0
    MaxMbHold = 0
    MaxMeshmaps = 0
    MaxMetricDispTypes = 0
    MaxOctaves = 0
    MaxPyramidDepth = 0
    MaxReleaseR10 = 0
    MaxReleaseR10Alpha = 0
    MaxReleaseR11 = 0
    MaxReleaseR11Alpha = 0
    MaxReleaseR12 = 0
    MaxReleaseR12Alpha = 0
    MaxReleaseR13 = 0
    MaxReleaseR13Alpha = 0
    MaxReleaseR14 = 0
    MaxReleaseR14Alpha = 0
    MaxReleaseR7 = 0
    MaxReleaseR8 = 0
    MaxReleaseR8Alpha = 0
    MaxReleaseR9 = 0
    MaxReleaseR9Alpha = 0
    MaxReleaseR9Alpha2 = 0
    MaxReleaseUnsupported = 0
    MaxSdkRev = 0
    MaxTrackViews = 0
    MaxTrackviewSelsets = 0
    MaxUnitdispTypes = 0
    MaxUnitTypes = 0
    MaxUsDispTypes = 0
    MaxVertdata = 0
    MbFlagChecked = 0
    MbFlagEnabled = 0
    MbTypeAction = 0
    MbTypeActionCustom = 0
    MbTypeKbd = 0
    MbTypeScript = 0
    McapIniChannel = 0
    McapIniPlay = 0
    McapIniPreset = 0
    McapIniRecord = 0
    McapIniSsenable = 0
    McapIniStop = 0
    McvFree = 0
    McvOriginal = 0
    MdeltaAll = 0
    MdeltaFchange = 0
    MdeltaFcreate = 0
    MdeltaFdata = 0
    MdeltaFdelete = 0
    MdeltaFremap = 0
    MdeltaFsmooth = 0
    MdeltaNumbers = 0
    MdeltaVclone = 0
    MdeltaVdata = 0
    MdeltaVdelete = 0
    MdeltaVmove = 0
    MduidEmAttach = 0
    MduidEmAttachList = 0
    MduidEmAutoedge = 0
    MduidEmAutosmooth = 0
    MduidEmBevel = 0
    MduidEmBreak = 0
    MduidEmChamfer = 0
    MduidEmCollapse = 0
    MduidEmCopyNamedsel = 0
    MduidEmCreate = 0
    MduidEmCut = 0
    MduidEmDetach = 0
    MduidEmDivide = 0
    MduidEmEdgeInvis = 0
    MduidEmEdgeVis = 0
    MduidEmExplode = 0
    MduidEmExtrude = 0
    MduidEmFlipnorm = 0
    MduidEmFlipNormalMode = 0
    MduidEmGridAlign = 0
    MduidEmHide = 0
    MduidEmIgback = 0
    MduidEmIgnoreInvis = 0
    MduidEmMakePlanar = 0
    MduidEmPasteNamedsel = 0
    MduidEmRefineCutends = 0
    MduidEmRemoveIso = 0
    MduidEmSelbyvert = 0
    MduidEmSelopen = 0
    MduidEmSeltype = 0
    MduidEmSeltypeBack = 0
    MduidEmSeltypeEdge = 0
    MduidEmSeltypeElement = 0
    MduidEmSeltypeFace = 0
    MduidEmSeltypeObj = 0
    MduidEmSeltypePolygon = 0
    MduidEmSeltypeVertex = 0
    MduidEmShownormal = 0
    MduidEmSlice = 0
    MduidEmSliceplane = 0
    MduidEmSoftsel = 0
    MduidEmSplit = 0
    MduidEmSsBackface = 0
    MduidEmTurnedge = 0
    MduidEmUnhide = 0
    MduidEmUnifyNormals = 0
    MduidEmVertColor = 0
    MduidEmVertIllum = 0
    MduidEmViewAlign = 0
    MduidEmWeld = 0
    MduidEmWeldTarget = 0
    MeDroppedScript = 0
    MeHasExecute = 0
    MeNeedsCompile = 0
    MeNoAutoUndo = 0
    MergeDupsDelold = 0
    MergeDupsMerge = 0
    MergeDupsPrompt = 0
    MergeDupsRename = 0
    MergeDupsSkip = 0
    MergeListNames = 0
    MergeReparentAlways = 0
    MergeReparentNever = 0
    MergeReparentPrompt = 0
    MeshBackfacescomputed = 0
    MeshBeenDsp = 0
    MeshboolDifference = 0
    MeshboolIntersection = 0
    MeshboolUnion = 0
    MeshCacheinvalid = 0
    MeshDispFaceNormals = 0
    MeshDispNoNormals = 0
    MeshDispVertexNormals = 0
    MeshDonttristrip = 0
    MeshEdge = 0
    MeshEdgeList = 0
    MeshFace = 0
    MeshFacenormalsinvalid = 0
    MeshLockRenddata = 0
    MeshmapTexture = 0
    MeshmapUsed = 0
    MeshmapUser = 0
    MeshmapVertcolor = 0
    MeshMultiProcessing = 0
    MeshNormalDisplayHandles = 0
    MeshNormalFaceAngles = 0
    MeshNormalModifierSupport = 0
    MeshNormalNormalsBuilt = 0
    MeshNormalNormalsComputed = 0
    MeshObject = 0
    MeshPartialcacheinvalid = 0
    MeshSelconvRequireAll = 0
    MeshSmoothBit1 = 0
    MeshSmoothBit2 = 0
    MeshSmoothBit3 = 0
    MeshSmoothBit4 = 0
    MeshSmoothMask = 0
    MeshSmoothSubsel = 0
    MeshTemp1 = 0
    MeshTemp2 = 0
    MeshUseExtCvarray = 0
    MeshVertex = 0
    MeSilentErrors = 0
    MeTemporary = 0
    MiddleButton = 0
    MirrorBoth = 0
    MirrorHorizontal = 0
    MirrorVertical = 0
    Mirrrored = 0
    MirrrorShared = 0
    MnBackfacing = 0
    MnCacheinvalid = 0
    MnDead = 0
    MndispBeenDisp = 0
    MndispDiagonals = 0
    MndispHideSubdivisionInteriors = 0
    MndispNormals = 0
    MndispSeledges = 0
    MndispSelfaces = 0
    MndispSelverts = 0
    MndispSmoothSubsel = 0
    MndispVertticks = 0
    MnEdgeCutExtra = 0
    MnEdgeInvis = 0
    MnEdgeMapSeam = 0
    MnEdgeNocross = 0
    MnEdgeSubdivisionBoundary = 0
    MnFaceChanged = 0
    MnFaceChecked = 0
    MnFaceCulled = 0
    MnFaceOpenRegion = 0
    MnHidden = 0
    MnHittestCulled = 0
    MnInforeground = 0
    MnLocalSel = 0
    MnMeshCacheFlags = 0
    MnMeshDonttristrip = 0
    MnMeshFaceNormalsInvalid = 0
    MnMeshFilledIn = 0
    MnMeshHasVolume = 0
    MnMeshHittestRequireAll = 0
    MnMeshNoBadVerts = 0
    MnMeshNontri = 0
    MnMeshPartialcacheinvalid = 0
    MnMeshRatsnest = 0
    MnMeshTemp1 = 0
    MnMeshTemp2 = 0
    MnMeshVertsOrdered = 0
    MnmSelconvRequireAll = 0
    MnnormalDisplayHandles = 0
    MnnormalFaceAngles = 0
    MnnormalNormalsBuilt = 0
    MnnormalNormalsComputed = 0
    MnSel = 0
    MnSelDefault = 0
    MnSelEdge = 0
    MnSelFace = 0
    MnSelObject = 0
    MnSelVertex = 0
    MnSubdivHideInternalEdges = 0
    MnSubdivNewmap = 0
    MnTarg = 0
    MnUser = 0
    MnVertDone = 0
    MnVertSubdivisionCorner = 0
    MnVertWelded = 0
    MnWhatever = 0
    ModeEditfcurve = 0
    ModeEditkeys = 0
    ModeEditranges = 0
    ModeEdittime = 0
    ModePosranges = 0
    ModifyCommand = 0
    MonoChannel = 0
    MotionCommand = 0
    MouseAbort = 0
    MouseAlt = 0
    MouseCaptureContinue = 0
    MouseContinue = 0
    MouseCtrl = 0
    MouseDblclick = 0
    MouseFreemove = 0
    MouseIdle = 0
    MouseInit = 0
    MouseKeyboard = 0
    MouseLbutton = 0
    MouseMbutton = 0
    MouseMove = 0
    MousePoint = 0
    MousePropclick = 0
    MouseRbutton = 0
    MouseShift = 0
    MouseSnapclick = 0
    MouseStop = 0
    MouseUninit = 0
    MoveButton = 0
    MoveCommand = 0
    MoveIntersection = 0
    MoveProjection = 0
    MszipfileDroptype = 0
    MtlBeingEdited = 0
    MtlBrowseOpen1 = 0
    MtlBrowseOpen2 = 0
    MtlChannel = 0
    MtlChanNum = 0
    MtlCloned = 0
    MtlDisplayEnableFlags = 0
    MtlHwMatEnabled = 0
    MtlHwMatPresent = 0
    MtlHwTexEnabled = 0
    MtlInScene = 0
    MtlMeditBackground = 0
    MtlMeditBacklight = 0
    MtlMeditObjtype = 0
    MtlMeditObjtypeMask = 0
    MtlMeditTiling = 0
    MtlMeditTilingMask = 0
    MtlMeditVidcheck = 0
    MtlObjtypeShift = 0
    Mtlreq2side = 0
    MtlreqAdditiveTransp = 0
    MtlreqAutomirror = 0
    MtlreqAutoreflect = 0
    MtlreqBgcol = 0
    MtlreqBumpuv = 0
    MtlreqBumpuv2 = 0
    MtlreqDisplacemap = 0
    MtlreqDontmergeFragments = 0
    MtlreqFacemap = 0
    MtlreqFaceted = 0
    MtlreqNoatmos = 0
    MtlreqNoexposure = 0
    MtlreqOxyz = 0
    MtlreqPhong = 0
    MtlreqPrepro = 0
    MtlreqRend1 = 0
    MtlreqRend2 = 0
    MtlreqRend3 = 0
    MtlreqRend4 = 0
    MtlreqSsGlobal = 0
    MtlreqSupersample = 0
    MtlreqTransp = 0
    MtlreqTranspInVp = 0
    MtlreqUv = 0
    MtlreqUv2 = 0
    MtlreqViewDep = 0
    MtlreqWire = 0
    MtlreqWireAbs = 0
    MtlreqWorldcoords = 0
    MtlreqXyz = 0
    MtlSubBeingEdited = 0
    MtlSubDisplayEnabled = 0
    MtlTexDisplayEnabled = 0
    MtlTilingShift = 0
    MtlWorkFlag = 0
    NewsetIntersection = 0
    NewsetMerge = 0
    NewsetSubtract = 0
    Next = 0
    NextkeyLeft = 0
    NextkeyPos = 0
    NextkeyRight = 0
    NextkeyRot = 0
    NextkeyScale = 0
    NgonCircular = 0
    NgonRadius = 0
    NgonSides = 0
    NIdChannels = 0
    NMaxRenderElements = 0
    NoClassdescIdReturned = 0
    NodeLayerRef = 0
    NoDialog = 0
    NoisemodAnimate = 0
    NoisemodFractal = 0
    NoisemodFreq = 0
    NoisemodIterations = 0
    NoisemodPhase = 0
    NoisemodRough = 0
    NoisemodScale = 0
    NoisemodSeed = 0
    NoisemodStrength = 0
    NoMirrror = 0
    NoMotblur = 0
    NorctMask = 0
    Normalcolor = 0
    NormalmodFlip = 0
    NormalmodUnify = 0
    Normalpressedcolor = 0
    NormmodFlip = 0
    NormmodUnify = 0
    NotekeyFlagged = 0
    NotekeyLocked = 0
    NotekeySelected = 0
    NotifyAll = 0
    NotifyCompletion = 0
    NotifyFailure = 0
    NotifyProgress = 0
    NotKeyframeable = 0
    Nshades = 0
    NsPoEdge = 0
    NsPoPatch = 0
    NsPoVert = 0
    NsSsPoly = 0
    NsSsSeg = 0
    NsSsVert = 0
    NtAffectIllum = 0
    NtAffectShadowcast = 0
    Ntexmaps = 0
    NtInclude = 0
    NullCommand = 0
    NumaxisAll = 0
    NumaxisIndividual = 0
    NumaxisZero = 0
    NumBuiltinDims = 0
    NumCamTypes = 0
    Numgbchan = 0
    NumHiddenmaps = 0
    NumLightTypes = 0
    Nummaskflags = 0
    NumObjChans = 0
    NumPatchPatchFlags = 0
    NumPatchVecFlags = 0
    NumPatchVertFlags = 0
    NumTangenttypes = 0
    NuscaleButton = 0
    ObjChannels = 0
    OmniLight = 0
    OpacityParam = 0
    OpentvCustom = 0
    OpentvLast = 0
    OpentvNew = 0
    OpentvSpecial = 0
    OptimizeAutoedge = 0
    OptimizeSavematboundries = 0
    OptimizeSavesmoothboundries = 0
    OptionalParam0 = 0
    OptionalParam1 = 0
    OptmodAutoedge = 0
    OptmodBias1 = 0
    OptmodBias2 = 0
    OptmodEdgethresh1 = 0
    OptmodEdgethresh2 = 0
    OptmodFacethresh1 = 0
    OptmodFacethresh2 = 0
    OptmodManupdate = 0
    OptmodMaxedge1 = 0
    OptmodMaxedge2 = 0
    OptmodPreservemat1 = 0
    OptmodPreservemat2 = 0
    OptmodPreservesmooth1 = 0
    OptmodPreservesmooth2 = 0
    OptmodRender = 0
    OptmodViews = 0
    OrientRotPblockRef = 0
    OriginLocal = 0
    OriginSelection = 0
    OriginSystem = 0
    OrtAfter = 0
    OrtBefore = 0
    OrtConstant = 0
    OrtCycle = 0
    OrtIdentity = 0
    OrtLinear = 0
    OrtLoop = 0
    OrtOscillate = 0
    OrtRelativeRepeat = 0
    OutBottom = 0
    OutCurvetangentChanged = 0
    OutLeft = 0
    OutortChunk = 0
    OutRight = 0
    OutTop = 0
    OwnerBrowseLib = 0
    OwnerBrowseMedit = 0
    OwnerBrowseNew = 0
    OwnerBrowseScene = 0
    OwnerMaterialExplorer = 0
    OwnerMeditSample = 0
    OwnerMtlTex = 0
    OwnerNode = 0
    OwnerScene = 0
    PaintcurveFrozen = 0
    PaintcurveFrozenkeys = 0
    PaintcurveGencolor = 0
    PaintcurveShowalltangents = 0
    PaintcurveShowtangents = 0
    PaintcurveSoftselect = 0
    PaintcurveWcolor = 0
    PaintcurveXcolor = 0
    PaintcurveYcolor = 0
    PaintcurveZcolor = 0
    PaintercanvasinterfaceV5 = 0
    PaintercanvasinterfaceV51 = 0
    PaintercanvasinterfaceV7 = 0
    PainterinterfaceV14 = 0
    PainterinterfaceV5 = 0
    PainterinterfaceV7 = 0
    PainttrackHidestaticvalues = 0
    PainttrackShowsel = 0
    PainttrackShowstats = 0
    PainttrackSubtreemode = 0
    PAnimatable = 0
    ParallelCamera = 0
    ParamNormalized = 0
    ParamSimple = 0
    ParmArclength = 0
    ParmCentripetal = 0
    ParmCustom = 0
    ParmUniform = 0
    PartcenterCenter = 0
    PartcenterHead = 0
    PartcenterTail = 0
    ParticleAges = 0
    ParticleRadius = 0
    ParticleTension = 0
    ParticleVels = 0
    PartPutInFg = 0
    PartShowDependencies = 0
    PartShowdepOn = 0
    PasteRelative = 0
    PatchAuto = 0
    PatchEdge = 0
    PatchgridLength = 0
    PatchgridLsegs = 0
    PatchgridTexture = 0
    PatchgridWidth = 0
    PatchgridWsegs = 0
    PatchHandle = 0
    PatchHidden = 0
    PatchHitEdge = 0
    PatchHitInterior = 0
    PatchHitPatch = 0
    PatchHitVector = 0
    PatchHitVertex = 0
    PatchInteriorMask = 0
    PatchLinearmapping = 0
    PatchManual = 0
    PatchMatidMask = 0
    PatchMatidShift = 0
    PatchObject = 0
    PatchPatch = 0
    PatchQuad = 0
    PatchTri = 0
    PatchUndef = 0
    PatchUndefined = 0
    PatchUseCurvedMappingOnVertexColor = 0
    PatchVertex = 0
    PathfileDroptype = 0
    PathposPathRef = 0
    PathposPblockRef = 0
    PAutoConstruct = 0
    PAutoUi = 0
    PbAnimatableChunk = 0
    PbBoolChunk = 0
    PbBoxgizmoHeight = 0
    PbBoxgizmoLength = 0
    PbBoxgizmoSeed = 0
    PbBoxgizmoWidth = 0
    PbCountChunk = 0
    PbCylgizmoHeight = 0
    PbCylgizmoRadius = 0
    PbCylgizmoSeed = 0
    PbFloatChunk = 0
    PbGizmoHemi = 0
    PbGizmoRadius = 0
    PbGizmoSeed = 0
    PbIndexChunk = 0
    PbIntChunk = 0
    PbLockedChunk = 0
    PbOsmtowsmDecay = 0
    PbOsmtowsmHeight = 0
    PbOsmtowsmLength = 0
    PbOsmtowsmWidth = 0
    PbParamChunk = 0
    PbPoint3Chunk = 0
    PbRgbaChunk = 0
    PbTypeBoolChunk = 0
    PbTypeChunk = 0
    PbTypeFloatChunk = 0
    PbTypeIntChunk = 0
    PbTypePoint3Chunk = 0
    PbTypeRgbaChunk = 0
    PbTypeUserChunk = 0
    PbVersionChunk = 0
    PCallsetsOnLoad = 0
    PCanConvert = 0
    PClassParams = 0
    PComputedName = 0
    PcvecNew = 0
    PcvecOriginal = 0
    PcvertFree = 0
    PcvertOriginal = 0
    PerdataTypeFloat = 0
    PHasAssettype = 0
    PHasAssettypename = 0
    PHasCaption = 0
    PHascategory = 0
    PHasClassId = 0
    PHasCurDefault = 0
    PHasDefault = 0
    PHasFiletypes = 0
    PHasMsDefault = 0
    PHasPrompt = 0
    PHasRange = 0
    PHasRefno = 0
    PHasSclassId = 0
    PHasSubtexno = 0
    PHasTooltip = 0
    PickCommand = 0
    PickExCommand = 0
    PicktrackFlagActivelayer = 0
    PicktrackFlagAnimated = 0
    PicktrackFlagBaseparams = 0
    PicktrackFlagBones = 0
    PicktrackFlagCameras = 0
    PicktrackFlagConttypes = 0
    PicktrackFlagFocusSelNodes = 0
    PicktrackFlagGeom = 0
    PicktrackFlagHelpers = 0
    PicktrackFlagHierarchy = 0
    PicktrackFlagKeyable = 0
    PicktrackFlagLights = 0
    PicktrackFlagLocked = 0
    PicktrackFlagMatmaps = 0
    PicktrackFlagMatparams = 0
    PicktrackFlagNodes = 0
    PicktrackFlagNotetracks = 0
    PicktrackFlagObjectmods = 0
    PicktrackFlagPosition = 0
    PicktrackFlagRotation = 0
    PicktrackFlagScale = 0
    PicktrackFlagSelobjects = 0
    PicktrackFlagShapes = 0
    PicktrackFlagSound = 0
    PicktrackFlagTransform = 0
    PicktrackFlagVisibleObjs = 0
    PicktrackFlagVistracks = 0
    PicktrackFlagWarps = 0
    PicktrackFlagWorldmods = 0
    PidsiContentstatus = 0
    PidsiContenttype = 0
    PidsiCreator = 0
    PidsiIdentifier = 0
    PidsiLanguage = 0
    PidsiVersion = 0
    PIncluded = 0
    PIncludeParams = 0
    PInvisible = 0
    PIsRef = 0
    PlaceButton = 0
    PlaceCommand = 0
    PmHittestRequireAll = 0
    PMultimap = 0
    PNoAutoLabels = 0
    PNoInit = 0
    PNoRef = 0
    PObsolete = 0
    PoEdge = 0
    PoElement = 0
    PoHandle = 0
    PointCollision = 0
    PointRgn = 0
    PoLevels = 0
    Polybool = 0
    Polyinside = 0
    PolylineClosed = 0
    PolylineNoSelfInt = 0
    PolyMultiProcessing = 0
    Polyoutside = 0
    PolyptBridge = 0
    PolyptInterpolated = 0
    PolyptInvisEdge = 0
    PolyptKnot = 0
    PolyptMatidMask = 0
    PolyptMatidShift = 0
    PolyptNoSnap = 0
    PolyptNoSplice = 0
    PolyptSegSelected = 0
    PolyptSmooth = 0
    PolyptSplice = 0
    PolyptVisedge = 0
    PolyshpInterpNormalized = 0
    PolyshpInterpSimple = 0
    PoObject = 0
    PoPatch = 0
    PosIdent = 0
    PositionDeriv = 0
    PosposPblockRef = 0
    PoVertex = 0
    POwnersRef = 0
    PReadOnly = 0
    PReadSecondFlagValue = 0
    PreNewKeepObjects = 0
    PreNewKeepObjectsAndHierarchy = 0
    PreNewNewAll = 0
    PResetDefault = 0
    PressureAffectsBoth = 0
    PressureAffectsNone = 0
    PressureAffectsSize = 0
    PressureAffectsStr = 0
    PreviewBefore = 0
    PreviewUp = 0
    PreviewWhole = 0
    ProjParallel = 0
    ProjPerspective = 0
    PropColor = 0
    PropidAppdata = 0
    PropidClearcaches = 0
    PropidCustattrib = 0
    PropidEaselist = 0
    PropidEvalStepsizeBugFixed = 0
    PropidForceRenderMeshCopy = 0
    PropidHardwareMaterial = 0
    PropidHasWsm = 0
    PropidInterpui = 0
    PropidJointparams = 0
    PropidKeyinfo = 0
    PropidMultlist = 0
    PropidNotetrack = 0
    PropidPinnode = 0
    PropidPrecedence = 0
    PropidPstampLarge = 0
    PropidPstampSmall = 0
    PropidPstampTiny = 0
    PropidRelpos = 0
    PropidRelrot = 0
    PropidSimpleMaterial = 0
    PropidSvdata = 0
    PropidUser = 0
    PropMaster = 0
    PropNodeBone = 0
    PropsetDocsummaryinfo = 0
    PropsetSummaryinfo = 0
    PropsetUserdefined = 0
    PScriptedClass = 0
    PshapeAdaptiveSteps = 0
    PshapeBuiltinSteps = 0
    PshapeSnapIgnorelast = 0
    PshapeSnapNoedges = 0
    PShortLabels = 0
    PsLarge = 0
    PsLargeSize = 0
    PsSmall = 0
    PsSmallSize = 0
    PsTiny = 0
    PsTinySize = 0
    PSubanim = 0
    PSubtex = 0
    PTemplateUi = 0
    PTemporary = 0
    PTransient = 0
    PTvShowAll = 0
    PUiEnabled = 0
    PUseAccessorOnly = 0
    PUseParams = 0
    PVariableSize = 0
    PvecInterior = 0
    PvecInteriorMask = 0
    PVersion = 0
    PvertCoplanar = 0
    PvertCorner = 0
    PvertHidden = 0
    PvertHiddenMask = 0
    PvertReset = 0
    PvertTypeMask = 0
    PwmfHasMenu = 0
    PwmfLeftTarget = 0
    PwmfOpenEditor = 0
    PwmfRightTarget = 0
    R3Adaptive = 0
    Rcbits = 0
    Rcfracmask = 0
    Rcoln = 0
    RcScl = 0
    RcSclhalf = 0
    Rcshmask = 0
    Rcshmax = 0
    ReallocSize = 0
    RectangleFillet = 0
    RectangleLength = 0
    RectangleWidth = 0
    RectLight = 0
    RectMask = 0
    RectRgn = 0
    RedrawBegin = 0
    RedrawEnd = 0
    RedrawInteractive = 0
    RedrawNormal = 0
    RedrawViews = 0
    RefEnumContinue = 0
    RefEnumHalt = 0
    RefEnumSkip = 0
    ReferenceMakerInterface = 0
    ReferenceTargetInterface = 0
    RefineSeg = 0
    RefineVert = 0
    ReflChannel = 0
    RefmsgBecomingAnimated = 0
    RefmsgBeforePaste = 0
    RefmsgBeginEdit = 0
    RefmsgBeginModifyParams = 0
    RefmsgBranchedHistoryChanged = 0
    RefmsgChange = 0
    RefmsgCheckForInvalidBind = 0
    RefmsgContainedShapeGeneralChange = 0
    RefmsgContainedShapePosChange = 0
    RefmsgContainedShapeSelChange = 0
    RefmsgContainerElementNulled = 0
    RefmsgControlrefChange = 0
    RefmsgCtrlxrefGetnodes = 0
    RefmsgDisable = 0
    RefmsgEnable = 0
    RefmsgEndEdit = 0
    RefmsgEndModifyParams = 0
    RefmsgEval = 0
    RefmsgFlagdependents = 0
    RefmsgFlagNodesWithSelDependents = 0
    RefmsgGetControlDim = 0
    RefmsgGetNodeHandle = 0
    RefmsgGetNodeName = 0
    RefmsgGetParamDim = 0
    RefmsgGetParamName = 0
    RefmsgInvalidateIfBg = 0
    RefmsgIsOkToChangeTopology = 0
    RefmsgKeySelectionChanged = 0
    RefmsgLineheightChange = 0
    RefmsgLocked = 0
    RefmsgLookatTargetDeleted = 0
    RefmsgLooptest = 0
    RefmsgModappDeleting = 0
    RefmsgModDisplayOff = 0
    RefmsgModDisplayOn = 0
    RefmsgModEval = 0
    RefmsgModifierAdded = 0
    RefmsgMouseCycleCompleted = 0
    RefmsgMouseCycleStarted = 0
    RefmsgMtlxrefGetnodes = 0
    RefmsgMxsCustattribChange = 0
    RefmsgNodeDisplayPropChanged = 0
    RefmsgNodeFlagombRender = 0
    RefmsgNodeGiPropChanged = 0
    RefmsgNodeHandleChanged = 0
    RefmsgNodeinselsetChanged = 0
    RefmsgNodeLink = 0
    RefmsgNodeMaterialChanged = 0
    RefmsgNodemonitorTargetDeleted = 0
    RefmsgNodeNamechange = 0
    RefmsgNodePreDelete = 0
    RefmsgNodeRenderingPropChanged = 0
    RefmsgNodetransformmonitorTargetDeleted = 0
    RefmsgNodeWirecolorChanged = 0
    RefmsgNodeWscacheUpdated = 0
    RefmsgNotifyPaste = 0
    RefmsgNumSubobjecttypesChanged = 0
    RefmsgObjectCacheDumped = 0
    RefmsgObjectDefinitionChangeBegin = 0
    RefmsgObjectDefinitionChangeEnd = 0
    RefmsgObjectReplaced = 0
    RefmsgObjxrefGetnodes = 0
    RefmsgObjxrefUpdatectrl = 0
    RefmsgObjxrefUpdatemat = 0
    RefmsgObrefChange = 0
    RefmsgPrenotifyPaste = 0
    RefmsgRangeChange = 0
    RefmsgRefAdded = 0
    RefmsgRefDeleted = 0
    RefmsgReftargmonitorTargetDeleted = 0
    RefmsgReftargmonitorTargetSet = 0
    RefmsgResetOrigin = 0
    RefmsgSelectBranch = 0
    RefmsgSelNodesDeleted = 0
    RefmsgSfxChange = 0
    RefmsgShapeEndChange = 0
    RefmsgShapeStartChange = 0
    RefmsgSubanimNumberChanged = 0
    RefmsgSubanimStructureChanged = 0
    RefmsgTargetDeleted = 0
    RefmsgTargetSelectionchange = 0
    RefmsgTestDependency = 0
    RefmsgTexmapRemoved = 0
    RefmsgTmChange = 0
    RefmsgTurnoff = 0
    RefmsgTurnon = 0
    RefmsgUnlocked = 0
    RefmsgUser = 0
    RefmsgUvSymChange = 0
    RefmsgWantShowparamlevel = 0
    RefrChannel = 0
    ReftargAutoDeleted = 0
    RenderbeginInMedit = 0
    RenderHideFrozen = 0
    RenderMeshDisplacementMap = 0
    RenderPresetsCategoryCount = 0
    RenderPresetsCustomCategoryIndexBegin = 0
    RenderPresetsSuccess = 0
    RenderR25shadows = 0
    RendmapShowNode = 0
    RendprogAbort = 0
    RendprogContinue = 0
    RendTimepickup = 0
    RendTimerange = 0
    RendTimesegment = 0
    RendTimesingle = 0
    Reset = 0
    RestobjDoesReferencePointer = 0
    RestobjGoingToDeletePointer = 0
    RgnDirLeft = 0
    RgnDirRight = 0
    RgnDirUndef = 0
    RightButton = 0
    Ringcolor = 0
    Ringpressedcolor = 0
    RndMask = 0
    RndNor0 = 0
    RollupCatCustattrib = 0
    RollupCatStandard = 0
    RollupCatSystem = 0
    RollupNoborder = 0
    RollupSavecat = 0
    RollupUsereplacedcat = 0
    RotateButton = 0
    RotateCommand = 0
    RotationDeriv = 0
    RotIdent = 0
    RpAntialiasOff = 0
    RpErrorCancel = 0
    RpErrorCategoryNotCompatable = 0
    RpErrorFileNotFound = 0
    RpErrorIncompatableFile = 0
    RpErrorLoadingFile = 0
    RpErrorObsoleteFile = 0
    RpErrorSavingFile = 0
    RspartBirthrate = 0
    RspartConstant = 0
    RspartDisptype = 0
    RspartDropsize = 0
    RspartEmitterheight = 0
    RspartEmitterwidth = 0
    RspartHideemitter = 0
    RspartLifetime = 0
    RspartRender = 0
    RspartRndparticles = 0
    RspartScale = 0
    RspartSpeed = 0
    RspartStarttime = 0
    RspartTumble = 0
    RspartVariation = 0
    RspartVptparticles = 0
    RwaveAmplitude = 0
    RwaveAmplitude2 = 0
    RwaveCircles = 0
    RwaveDecay = 0
    RwaveDivisions = 0
    RwaveFlex = 0
    RwavePhase = 0
    RwaveSegments = 0
    RwaveWavelen = 0
    SamplerbaseChunk = 0
    SamplernameChunk = 0
    SamplerVersChunk = 0
    ScaleCommand = 0
    SceneDisplacement = 0
    SceneDither256 = 0
    SceneDithertrue = 0
    SceneEffects = 0
    SceneExportSelected = 0
    SceneFieldorder = 0
    ScenefileDroptype = 0
    SceneRenderatmospher = 0
    SceneRenderfields = 0
    SceneRenderhiden = 0
    SceneSerialnumbering = 0
    ScenestatePartsCount = 0
    SceneSuperblack = 0
    SceneTwosided = 0
    SceneVideocolorcheck = 0
    SclIdent = 0
    ScmodeNormal = 0
    ScmodeShadow = 0
    ScopeAll = 0
    ScopeChildren = 0
    ScopeDoclosed = 0
    ScopeOpen = 0
    ScopeSubanim = 0
    ScriptfileDroptype = 0
    SegmentVisible = 0
    SelectButton = 0
    SelectChannel = 0
    SelectChanNum = 0
    SelectCommand = 0
    SelfillumClrOn = 0
    SelkeysClearcurve = 0
    SelkeysClearkeys = 0
    SelkeysDeselect = 0
    SelkeysFcurve = 0
    SelkeysSelect = 0
    SelptsClearpts = 0
    SelptsDeselect = 0
    SelptsSelect = 0
    SetkeyAll = 0
    SetkeyAttributes = 0
    SetkeyIkParams = 0
    SetkeyMaterial = 0
    SetkeyModifier = 0
    SetkeyObjparams = 0
    SetkeyOther = 0
    SetkeyPos = 0
    SetkeyRot = 0
    SetkeyScale = 0
    SetkeySelectedNodes = 0
    SetkeySettingKeys = 0
    SetParamsAbsolute = 0
    SetParamsRelative = 0
    SfxbaseChunk = 0
    SfxnameChunk = 0
    Shad2sided = 0
    ShadeBlinn = 0
    ShadeConst = 0
    ShadecontextBounceMask = 0
    ShadecontextGuessShadowsFlag = 0
    ShadecontextPrepassFlag = 0
    ShadecontextRecursiveEvalFlag = 0
    ShadecontextRegatheringFlag = 0
    ShadecontextThreadMask = 0
    ShadecontextThreadShift = 0
    ShadecontextWorkerMask = 0
    ShadecontextWorkerShift = 0
    ShadeLevels = 0
    ShadelimFlat = 0
    ShadelimGouraud = 0
    ShadelimPhong = 0
    ShadeMetal = 0
    ShadePhong = 0
    ShaderbaseChunk = 0
    ShadernameChunk = 0
    ShadOmni = 0
    ShadParallel = 0
    ShapeExtend = 0
    ShapeObject = 0
    ShapeObjNumRefs = 0
    ShapeObjNumSubs = 0
    Shapeobjpblock = 0
    ShapeRectRenderparamsPropid = 0
    ShapeSegment = 0
    ShapeSpline = 0
    ShapeTrim = 0
    ShapeVertex = 0
    ShowCursor = 0
    ShowPreview = 0
    SimpmodPblockref = 0
    SimpwsmmodNoderef = 0
    SimpwsmmodObref = 0
    SimpwsmmodPblockref = 0
    SketchApplymode = 0
    SketchBox = 0
    SketchCircle = 0
    SketchDrawmode = 0
    SketchFreeform = 0
    SketchLine = 0
    SketchSelcurrent = 0
    SketchSeldrag = 0
    SketchSelpick = 0
    SkewAmount = 0
    SkewAxis = 0
    SkewDir = 0
    SkewDoregion = 0
    SkewFrom = 0
    SkewTo = 0
    SkinInvalidNodePtr = 0
    SkinOk = 0
    SkipChannels = 0
    SlevChannel = 0
    SmallVertexDots = 0
    SmoothAutosmooth = 0
    SmoothmodAutosmooth = 0
    SmoothmodSmoothbits = 0
    SmoothmodThreshold = 0
    SmoothSmoothbits = 0
    SmoothThreshold = 0
    Snap25d = 0
    Snap2d = 0
    Snap3d = 0
    SnapApplyConstraints = 0
    SnapBeginSeq = 0
    SnapEndSeq = 0
    SnapForce3dResult = 0
    SnapFrozen = 0
    SnapIn3d = 0
    SnapInPlane = 0
    SnapmodeAbsolute = 0
    SnapmodeRelative = 0
    SnapOffPlane = 0
    SnapProjXaxis = 0
    SnapProjYaxis = 0
    SnapProjZaxis = 0
    SnapSelObjsOnly = 0
    SnapSelSubobjOnly = 0
    SnapTransparently = 0
    SnapUnselObjsOnly = 0
    SnapUnselSubobjOnly = 0
    SnapUseXformAxisAsStartSnapPoint = 0
    SnapXformAxis = 0
    SoCenterPivot = 0
    SoCenterSelection = 0
    SpacewarpCatGeomdef = 0
    SpacewarpCatModbased = 0
    SpacewarpCatParticle = 0
    SpecifiedNormal = 0
    SphereCollision = 0
    SphereGenuvs = 0
    SphereHemi = 0
    SphereRadius = 0
    SphereRecenter = 0
    SphereSegs = 0
    SphereSmooth = 0
    SphereSquash = 0
    SpinnerWrapDistance = 0
    SplineClosed = 0
    SplineikcontrolPblockRef = 0
    SplineInterpNormalized = 0
    SplineInterpSimple = 0
    SplineknotAddSel = 0
    SplineknotNoSnap = 0
    SplineMatidMask = 0
    SplineMatidShift = 0
    SplineOrthog = 0
    SpotlightCommand = 0
    SquashButton = 0
    SquashCommand = 0
    SsObject = 0
    SsSegment = 0
    SsSpline = 0
    SsVertex = 0
    StackDepth = 0
    StartDistort = 0
    StartFillet1 = 0
    StartFillet2 = 0
    StartPoints = 0
    StartRadius1 = 0
    StartRadius2 = 0
    StatusAngle = 0
    StatusOther = 0
    StatusPolar = 0
    StatusPolarRelative = 0
    StatusScale = 0
    StatusUniverse = 0
    StatusUniverseRelative = 0
    Std2NmaxTexmaps = 0
    StdAniso = 0
    StdBasic = 0
    StdBasic2Dlg = 0
    StdBasicMetal = 0
    StdExtraDlg = 0
    StdExtraOpacity = 0
    StdExtraReflection = 0
    StdExtraRefraction = 0
    StdMultilayer = 0
    StdOnb = 0
    StdParamAll = 0
    StdParamAmbientClr = 0
    StdParamAniso = 0
    StdParamDiffuseClr = 0
    StdParamDiffuseLev = 0
    StdParamDiffuseRho = 0
    StdParamFilterClr = 0
    StdParamGlossiness = 0
    StdParamLockad = 0
    StdParamLockadtex = 0
    StdParamLockds = 0
    StdParamMetal = 0
    StdParamNone = 0
    StdParamOrientation = 0
    StdParamReflLev = 0
    StdParamSelfillum = 0
    StdParamSelfillumClr = 0
    StdParamSelfillumClrOn = 0
    StdParamSoftenLev = 0
    StdParamSpecularClr = 0
    StdParamSpecularLev = 0
    StdWard = 0
    SubdivEdges = 0
    SubdivPatches = 0
    SubhitAbortonhit = 0
    SubhitEdges = 0
    SubhitFaces = 0
    SubhitMndiagonals = 0
    SubhitMnedges = 0
    SubhitMnfaces = 0
    SubhitMntypemask = 0
    SubhitMnusecurrentsel = 0
    SubhitMnverts = 0
    SubhitOpenonly = 0
    SubhitPatchAbortonhit = 0
    SubhitPatchEdges = 0
    SubhitPatchIgnoreBackfacing = 0
    SubhitPatchPatches = 0
    SubhitPatchSelonly = 0
    SubhitPatchSelsolid = 0
    SubhitPatchTypemask = 0
    SubhitPatchUnselonly = 0
    SubhitPatchVecs = 0
    SubhitPatchVerts = 0
    SubhitSelonly = 0
    SubhitSelsolid = 0
    SubhitShapeAbortonhit = 0
    SubhitShapePolys = 0
    SubhitShapeSegments = 0
    SubhitShapeSelonly = 0
    SubhitShapeSelsolid = 0
    SubhitShapeTypemask = 0
    SubhitShapeUnselonly = 0
    SubhitShapeVerts = 0
    SubhitTypemask = 0
    SubhitUnselonly = 0
    SubhitUsefacesel = 0
    SubhitVerts = 0
    SubselTypeChannel = 0
    SubselTypeChanNum = 0
    SuperSampleTexCheckBox = 0
    SurfcontSurfobjRef = 0
    SurfcontURef = 0
    SurfcontVRef = 0
    SurfrevCapend = 0
    SurfrevCapstart = 0
    SurfrevCaptype = 0
    SurfrevDegrees = 0
    SurfrevMapping = 0
    SurfrevOutput = 0
    SurfrevSegs = 0
    SurfrevWeldcore = 0
    SyscurDefarrow = 0
    SyscurMove = 0
    SyscurMoveSnap = 0
    SyscurNuscale = 0
    SyscurRotate = 0
    SyscurSelect = 0
    SyscurSquash = 0
    SyscurUscale = 0
    SyslogBroadcast = 0
    SyslogDebug = 0
    SyslogError = 0
    SyslogInfo = 0
    SyslogLifeDays = 0
    SyslogLifeEver = 0
    SyslogLifeSize = 0
    SyslogMr = 0
    SyslogWarn = 0
    SyssetClearUndo = 0
    SyssetEditablemeshEnableKeyboardAccel = 0
    SyssetEnableEditablemesh = 0
    SyssetEnableEditmeshmod = 0
    SystemLockReturn = 0
    SystemRemoteReturn = 0
    TaperAmt = 0
    TaperAxis = 0
    TaperCrv = 0
    TaperDoregion = 0
    TaperEffectaxis = 0
    TaperFrom = 0
    TaperSymmetry = 0
    TaperTo = 0
    TargetedCamera = 0
    TargetmsgAttachingNode = 0
    TargetmsgDeletingNode = 0
    TargetmsgDetachingNode = 0
    TargetmsgUser = 0
    TaskModeCreate = 0
    TaskModeDisplay = 0
    TaskModeHierarchy = 0
    TaskModeModify = 0
    TaskModeMotion = 0
    TaskModeUtility = 0
    TbRightclick = 0
    TcbkeyQuatvalid = 0
    TdirLight = 0
    TeapotBody = 0
    TeapotGenuvs = 0
    TeapotHandle = 0
    TeapotLid = 0
    TeapotRadius = 0
    TeapotSegs = 0
    TeapotSmooth = 0
    TeapotSpout = 0
    TeapotTeapart = 0
    TessmodFaceType = 0
    TessmodIterations = 0
    TessmodTension = 0
    TessmodType = 0
    TexmapChannel = 0
    TexmapChanNum = 0
    TexoutAlphaRgb = 0
    TexoutClamp = 0
    TexoutColorMap = 0
    TexoutColorMapRgb = 0
    TexoutInvert = 0
    TexoutXxxxx = 0
    TextKerning = 0
    TextLeading = 0
    TextobjCenter = 0
    TextobjItalic = 0
    TextobjJustified = 0
    TextobjLeft = 0
    TextobjRight = 0
    TextobjUnderline = 0
    TextSize = 0
    TflagColor = 0
    TflagCurvesel = 0
    TflagHsv = 0
    TflagLoopedin = 0
    TflagLoopedout = 0
    TflagNotkeyable = 0
    TflagRangeUnlocked = 0
    TflagTcbquatNowindup = 0
    tuple  th0
    TimeIncleft = 0
    TimeIncright = 0
    TimeNoslide = 0
    TimerangeAll = 0
    TimerangeChildanims = 0
    TimerangeChildnodes = 0
    TimerangeSelonly = 0
    TimesliderRbuttonDown = 0
    TimeTickspersec = 0
    TmChannel = 0
    TopoChannel = 0
    TopoChanNum = 0
    TorusGenuvs = 0
    TorusPieslice1 = 0
    TorusPieslice2 = 0
    TorusRadius = 0
    TorusRadius2 = 0
    TorusRotation = 0
    TorusSegments = 0
    TorusSides = 0
    TorusSliceon = 0
    TorusSmooth = 0
    TorusTwist = 0
    Tracecolor = 0
    TrackAskclient = 0
    TrackbarFilterAll = 0
    TrackbarFilterCurrenttm = 0
    TrackbarFilterMaterial = 0
    TrackbarFilterObject = 0
    TrackbarFilterTmonly = 0
    TrackDoall = 0
    TrackDochildnodes = 0
    TrackDone = 0
    TrackDorange = 0
    TrackDosel = 0
    TrackDosoftselect = 0
    TrackDostandard = 0
    TrackDosubanims = 0
    TrackInsertkeys = 0
    TrackMaprange = 0
    TrackparamsKey = 0
    TrackparamsNone = 0
    TrackparamsWhole = 0
    TrackReplacekeys = 0
    TrackRighttoleft = 0
    TrackSlideunsel = 0
    TrackviewAnim = 0
    TrackviewNode = 0
    TrackXlocked = 0
    TransformCmdSuper = 0
    TranspAdditive = 0
    TranspFilter = 0
    TranspSubtractive = 0
    TraverseHifiltshadows = 0
    TraverseLowfiltshadows = 0
    TraverseUsesamplesize = 0
    TreeAbort = 0
    TreeContinue = 0
    TreeIgnorechildren = 0
    TriMultiProcessing = 0
    TspotLight = 0
    TubeCapsegments = 0
    TubeGenuvs = 0
    TubeHeight = 0
    TubePieslice1 = 0
    TubePieslice2 = 0
    TubeRadius = 0
    TubeRadius2 = 0
    TubeSegments = 0
    TubeSides = 0
    TubeSliceon = 0
    TubeSmooth = 0
    TvCanDockTop = 0
    TvDockBottom = 0
    TvDockTop = 0
    TvFloat = 0
    TvmodeEditfcurve = 0
    TvmodeEditkeys = 0
    TvmodeEditranges = 0
    TvmodeEdittime = 0
    TvmodePosranges = 0
    TvnodeAppend = 0
    TvstyleInmotionpan = 0
    TvstyleInviewport = 0
    TvstyleMaximizebut = 0
    TvstyleNameable = 0
    TvstyleShowCui = 0
    TvstyleShowNonanimatable = 0
    TwistAngle = 0
    TwistAxis = 0
    TwistBias = 0
    TwistDoregion = 0
    TwistFrom = 0
    TwistTo = 0
    TwoSidedShadowDefault = 0
    TypeByPtr = 0
    TypeByRef = 0
    TypeByVal = 0
    TypeInvalidXrefFiles = 0
    TypeMissingDllFiles = 0
    TypeMissingExternalFiles = 0
    TypeMissingUvws = 0
    TypeMissingXrefFiles = 0
    TypeTab = 0
    TypeUnsupportedRendereffect = 0
    UMirror = 0
    UndefFace = 0
    UnitDesigCm = 0
    UnitDesigCustom = 0
    UnitDesigFt = 0
    UnitDesigIn = 0
    UnitDesigKm = 0
    UnitDesigM = 0
    UnitDesigMm = 0
    UnitDesigTypes = 0
    UnitdispCustom = 0
    UnitdispGeneric = 0
    UnitdispMetric = 0
    UnitdispUs = 0
    UnitFrac11 = 0
    UnitFrac110 = 0
    UnitFrac1100 = 0
    UnitFrac116 = 0
    UnitFrac12 = 0
    UnitFrac132 = 0
    UnitFrac14 = 0
    UnitFrac164 = 0
    UnitFrac18 = 0
    UnitMetricDispCm = 0
    UnitMetricDispKm = 0
    UnitMetricDispM = 0
    UnitMetricDispMm = 0
    UnitsCentimeters = 0
    UnitsFeet = 0
    UnitsInches = 0
    UnitsKilometers = 0
    UnitsMeters = 0
    UnitsMiles = 0
    UnitsMillimeters = 0
    UnitUsDispDecFt = 0
    UnitUsDispDecIn = 0
    UnitUsDispFracFt = 0
    UnitUsDispFracIn = 0
    UnitUsDispFtDecIn = 0
    UnitUsDispFtFracIn = 0
    UnsupportedChannel = 0
    UscaleButton = 0
    UscaleCommand = 0
    UseDamageRect = 0
    UsUnitDefaultFeet = 0
    UsUnitDefaultInches = 0
    UvmapCylEnv = 0
    UvmapExplicit = 0
    UvmapScreenEnv = 0
    UvmapShrinkEnv = 0
    UvmapSphereEnv = 0
    UvNoise = 0
    UvNoiseAni = 0
    UvsourceFacemap = 0
    UvsourceHwgen = 0
    UvsourceMesh = 0
    UvsourceMesh2 = 0
    UvsourceWorldxyz = 0
    UvsourceXyz = 0
    Uvw2Coords = 0
    UvwCoords = 0
    UvwmapAxis = 0
    UvwmapCap = 0
    UvwmapChannel = 0
    UvwmapHeight = 0
    UvwmapLength = 0
    UvwmapMaptype = 0
    UvwmapUflip = 0
    UvwmapUtile = 0
    UvwmapVflip = 0
    UvwmapVtile = 0
    UvwmapWflip = 0
    UvwmapWidth = 0
    UvwmapWtile = 0
    UvwsrcExplicit = 0
    UvwsrcExplicit2 = 0
    UvwsrcFacemap = 0
    UvwsrcHwgen = 0
    UvwsrcObjxyz = 0
    UvwsrcWorldxyz = 0
    UvwxformChannel = 0
    UvwxformUflip = 0
    UvwxformUoffset = 0
    UvwxformUtile = 0
    UvwxformVflip = 0
    UvwxformVoffset = 0
    UvwxformVtile = 0
    UvwxformWflip = 0
    UvwxformWoffset = 0
    UvwxformWtile = 0
    UWrap = 0
    VdataAlpha = 0
    VdataCorner = 0
    VdataSelect = 0
    VdataUser = 0
    VdataWeight = 0
    Version3dsmax = 0
    VersionInt = 0
    VertcolorChannel = 0
    VertColorChanNum = 0
    VertexDot2 = 0
    VertexDot3 = 0
    VertexDot4 = 0
    VertexDot5 = 0
    VertexDot6 = 0
    VertexDot7 = 0
    ViewportBkgAspectBitmap = 0
    ViewportBkgAspectOutput = 0
    ViewportBkgAspectView = 0
    ViewportBkgBlank = 0
    ViewportBkgEnd = 0
    ViewportBkgHold = 0
    ViewportBkgLoop = 0
    ViewportBkgStart = 0
    ViewportCommand = 0
    VisBit = 0
    VisMask = 0
    VMirror = 0
    VolselInvert = 0
    VolselLevel = 0
    VolselMethod = 0
    VolselType = 0
    VolselVolume = 0
    VpDefaultRender = 0
    VpDontRender = 0
    VpDontSimplify = 0
    VpEndSequence = 0
    VpLayout1 = 0
    VpLayout1c = 0
    VpLayout2h = 0
    VpLayout2hb = 0
    VpLayout2ht = 0
    VpLayout2v = 0
    VpLayout3hb = 0
    VpLayout3ht = 0
    VpLayout3vl = 0
    VpLayout3vr = 0
    VpLayout4 = 0
    VpLayout4hb = 0
    VpLayout4ht = 0
    VpLayout4vl = 0
    VpLayout4vr = 0
    VpNumViewsMask = 0
    VpSecondPass = 0
    VpStartSequence = 0
    VptTransBlend = 0
    VptTransNone = 0
    VptTransSortBlend = 0
    VptTransStipple = 0
    VWrap = 0
    WindDecay = 0
    WindDisplength = 0
    WindFrequency = 0
    WindScale = 0
    WindStrength = 0
    WindTurbulence = 0
    WindType = 0
    WmAddColor = 0
    WmBvToolbarRightclick = 0
    WmCcChangeCurvept = 0
    WmCcChangeCurvetangent = 0
    WmCcDelCurvept = 0
    WmCcInsertCurvept = 0
    WmCcLbuttondown = 0
    WmCcLbuttonup = 0
    WmCcRbuttondown = 0
    WmCcSelCurvept = 0
    WmCusteditEnter = 0
    WmCustrollupRecalclayout = 0
    WmInitComplete = 0
    WmMouseabort = 0
    WmSettcbgraphparams = 0
    WmShutdown = 0
    WmSubMtlButton = 0
    WmTexmapButton = 0
    WmTvDohzoomextents = 0
    WmTvLabelDoubleClick = 0
    WmTvMeditTvDestroyed = 0
    WmTvSelchanged = 0
    WmTvToolbarRightclick = 0
    Wrdmax = 0
    XAxis = 0
    XdataAppname = 0
    XdataEntry = 0
    XrefAsProxy = 0
    XrefBoxDisp = 0
    XrefDisabled = 0
    XrefDropModifiers = 0
    XrefFileChange = 0
    XrefHidden = 0
    XrefIgnoreAnim = 0
    XrefIgnoreCameras = 0
    XrefIgnoreHelpers = 0
    XrefIgnoreLights = 0
    XrefIgnoreShapes = 0
    XrefLoadError = 0
    XrefMergeControllers = 0
    XrefMergeManipulators = 0
    XrefMergeMaterials = 0
    XrefMergeModifiers = 0
    XrefSceneHideinmanagerui = 0
    XrefSceneOverlay = 0
    XrefSelectNodes = 0
    XrefUpdateAuto = 0
    XrefXrefModifiers = 0
    XyzConstraint = 0
    XyzCoords = 0
    XyzWorldCoords = 0
    YAxis = 0
    ZAxis = 0
    ZoomextNo = 0
    ZoomextNotImplemented = 0
    ZoomextYes = 0


class ContainerManager:
    AsContainer = ()

    AsContainerNode = ()

    CreateContainer = ()

    CreateInheritedContainer = ()

    GetContainer = ()

    IsContainerNode = ()

    IsInContainer = ()

    thisown = ()

    def AsContainer(self):
        pass

    def AsContainerNode(self):
        pass

    def CreateContainer(self):
        pass

    def CreateInheritedContainer(self):
        pass

    def GetContainer(self):
        pass

    def IsContainerNode(self):
        pass

    def IsInContainer(self):
        pass


class ContainerObject(FPInterface):
    AnythingUnlocked = 0

    LockAllMaterials = 0

    LockAllModifiers = 0

    LockAllObjects = 0

    LockAllTransforms = 0

    NoAccess = 0

    OnlyAddNewObjects = 0

    OnlyEditInPlace = 0

    PROXYTYPE_ALTERNATE = 0

    PROXYTYPE_NONE = 0

    thisown = ()

    def AddNodesToContent(self):
        pass

    def AddNodeToContent(self):
        pass

    def AllowInPlaceEdit(self):
        pass

    def AppendAlternateDefinition(self):
        pass

    def AutoUpdateClosed(self):
        pass

    def CanEditInPlace(self):
        pass

    def ClearLockedContents(self):
        pass

    def GetAccessType(self):
        pass

    def GetAllowInPlaceEdit(self):
        pass

    def GetAlternateDefinition(self):
        pass

    def GetAlternateDefinitionCount(self):
        pass

    def GetContainerNode(self):
        pass

    def GetContentNodes(self):
        pass

    def GetCurrentAlternateDefinition(self):
        pass

    def GetCurrentAlternateDefinitionIndex(self):
        pass

    def GetDesc(self):
        pass

    def GetEditingUser(self):
        pass

    def GetLabelDisplay(self):
        pass

    def GetLocalDefinitionFileName(self):
        pass

    def GetProxyType(self):
        pass

    def GetSize(self):
        pass

    def GetSourceDefinitionFileName(self):
        pass

    def GetStatusDisplay(self):
        pass

    def GetStatusString(self):
        pass

    def InheritedAccessType(self):
        pass

    def IsContainerOpenableOrClosable(self):
        pass

    def IsInherited(self):
        pass

    def IsInheritedClosed(self):
        pass

    def IsInPlaceEditing(self):
        pass

    def IsLockedContents(self):
        pass

    def IsNodeInContent(self):
        pass

    def IsNodeInInheritedContent(self):
        pass

    def IsOpen(self):
        pass

    def IsUnique(self):
        pass

    def IsUnloaded(self):
        pass

    def IsUpdateNeeded(self):
        pass

    def IsUsingContentBoundingBox(self):
        pass

    def LoadContainer(self):
        pass

    def MakeUnique(self):
        pass

    def MergeSource(self):
        pass

    def OverrideNodeProperties(self):
        pass

    def ReloadContainer(self):
        pass

    def RemoveAlternateDefinition(self):
        pass

    def RemoveNodeFromContent(self):
        pass

    def SaveContainer(self):
        pass

    def SaveContainerAsVersion(self):
        pass

    def SetAccessType(self):
        pass

    def SetAlternateDefinition(self):
        pass

    def SetAutoUpdateClosed(self):
        pass

    def SetCurrentAlternateDefinitionIndex(self):
        pass

    def SetEditInPlace(self):
        pass

    def SetLabelDisplay(self):
        pass

    def SetLocalDefinitionFileName(self):
        pass

    def SetLockedContents(self):
        pass

    def SetOpen(self):
        pass

    def SetOverrideNodeProperties(self):
        pass

    def SetProxyType(self):
        pass

    def SetSize(self):
        pass

    def SetSourceDefinitionFileName(self):
        pass

    def SetStatusDisplay(self):
        pass

    def UnloadContainer(self):
        pass

    def UpdateContainer(self):
        pass

    def UseContentBoundingBox(self):
        pass


class ContainerPreferences:
    Always = 0
    Never = 0
    PerContainer = 0
    thisown = ()
    def DisplayStatus(self):
        pass

    def NoUpdateCheck(self):
        pass

    def SaveAsPreviousAccessType(self):
        pass

    def SetDisplayStatus(self):
        pass

    def SetNoUpdateCheck(self):
        pass

    def SetSaveAsPreviousAccessType(self):
        pass

    def SetStatusUpdateInterval(self):
        pass

    def SetUpdateOnLoad(self):
        pass

    def SetUpdateOnReload(self):
        pass

    def StatusUpdateInterval(self):
        pass

    def UpdateOnLoad(self):
        pass

    def UpdateOnReload(self):
        pass


class ControlList:
    this = 0

    def Append(self):
        pass

    def Delete(self):
        pass

    def GetCount(self):
        pass

    def GetItem(self):
        pass

    def Insert(self):
        pass

    def SetCount(self):
        pass

    def SetItem(self):
        pass


class CoordinateSystem:
    AddReferencedNode = ()

    EnableCenter = ()

    EnableReferenceSystem = ()

    GetCenter = ()

    GetCurrent = ()

    GetReferenceNode = ()

    GetReferenceSystem = ()

    SetCenter = ()

    SetReferenceSystem = ()

    thisown = ()

    def AddReferencedNode(self):
        pass

    def EnableCenter(self):
        pass

    def EnableReferenceSystem(self):
        pass

    def GetCenter(self):
        pass

    def GetCurrent(self):
        pass

    def GetReferenceNode(self):
        pass

    def GetReferenceSystem(self):
        pass

    def SetCenter(self):
        pass

    def SetReferenceSystem(self):
        pass



class Core:
    EvalMAXScript = ()

    GetCOREInterface = ()

    GetCOREInterfaceAt = ()

    GetCurrentTime = ()

    GetFPInterface = ()

    GetFPInterfaceDesc = ()

    GetInterface = ()

    GetRootNode = ()

    GetWindowHandle = ()

    Print = ()

    SetCurrentTime = ()

    Write = ()

    WriteLine = ()

    def EvalMAXScript(self, string, FPValue):
        pass

    def GetCOREInterface(self, Interface_ID):
        return FPInterface()

    def GetCOREInterfaceAt(self,int):
        return FPInterface()

    def GetCurrentTime(self):
        return TimeValue()

    def GetFPInterface(self, BaseInterface):
        return FPInterface()

    def GetFPInterfaceDesc(self, BaseInterface):
        return FPInterfaceDesc()

    def GetInterface(self,SClass_ID, Class_ID, Interface_ID):
        return FPInterface()

    def GetRootNode(self):
        return INode()

    def GetWindowHandle(self):
        return 0

    def Print(self, string):
        pass

    def SetCurrentTime(self, TimeValue):
        pass

    def Write(self, string):
        pass

    def WriteLine(self, string):
        pass


class CUI:
    AreAcceleratorsEnabled = ()

    AreAllFloatersHidden = ()

    DisableAccelerators = ()

    DoUICustomization = ()

    EnableAccelerators = ()

    EnableToolButton = ()

    GetActionCommonIReshadeTableId = ()

    GetActionIReshadeContext = ()

    GetActionMainUIContext = ()

    GetActionMainUITableId = ()

    GetActionMaterialEditorContext = ()

    GetActionMaterialEditorTableId = ()

    GetActionScanlineIReshadeTableId = ()

    GetActionSchematicViewContext = ()

    GetActionSchematicViewTableId = ()

    GetActionTrackViewContext = ()

    GetActionTrackViewTableId = ()

    GetActionVideoPostContext = ()

    GetActionVideoPostTableId = ()

    GetCancel = ()

    GetExpertMode = ()

    GetFlyOffTime = ()

    GetToolButtonState = ()

    LoadCUI = ()

    LoadCUIConfig = ()

    ResetToFactoryDefaultCUI = ()

    RevertToBackupCUI = ()

    SaveCUIAs = ()

    SetCancel = ()

    SetExpertMode = ()

    SetFlyOffTime = ()

    SetToolButtonState = ()

    ShowCustomizeDialog = ()

    WriteCUIConfig = ()

    def AreAcceleratorsEnabled(self):
        pass

    def AreAllFloatersHidden(self):
        pass

    def DisableAccelerators(self):
        pass

    def DoUICustomization(self):
        pass

    def EnableAccelerators(self):
        pass

    def EnableToolButton(self):
        pass

    def GetActionCommonIReshadeTableId(self):
        pass

    def GetActionIReshadeContext(self):
        pass

    def GetActionMainUIContext(self):
        pass

    def GetActionMainUITableId(self):
        pass

    def GetActionMaterialEditorContext(self):
        pass

    def GetActionMaterialEditorTableId(self):
        pass

    def GetActionScanlineIReshadeTableId(self):
        pass

    def GetActionSchematicViewContext(self):
        pass

    def GetActionSchematicViewTableId(self):
        pass

    def GetActionTrackViewContext(self):
        pass

    def GetActionTrackViewTableId(self):
        pass

    def GetActionVideoPostContext(self):
        pass

    def GetActionVideoPostTableId(self):
        pass

    def GetCancel(self):
        pass

    def GetExpertMode(self):
        pass

    def GetFlyOffTime(self):
        pass

    def GetToolButtonState(self):
        pass

    def LoadCUI(self):
        pass

    def LoadCUIConfig(self):
        pass

    def ResetToFactoryDefaultCUI(self):
        pass

    def RevertToBackupCUI(self):
        pass

    def SaveCUIAs(self):
        pass

    def SetCancel(self):
        pass

    def SetExpertMode(self):
        pass

    def SetFlyOffTime(self):
        pass

    def SetToolButtonState(self):
        pass

    def ShowCustomizeDialog(self):
        pass

    def WriteCUIConfig(self):
        pass


class CUIFrameMgr:
    DrawCUIWindows = ()

    Frames = ()

    GetConfigFile = ()

    GetCount = ()

    GetCUIDirectory = ()

    GetFrame = ()

    RecalcLayout = ()

    ResetIconImages = ()

    SetConfigFile = ()

    SetMacroButtonStates = ()

    thisown = ()

    def DrawCUIWindows(self):
        pass

    def GetConfigFile(self):
        pass

    def GetCount(self):
        pass

    def GetCUIDirectory(self):
        pass

    def GetFrame(self):
        pass

    def RecalcLayout(self):
        pass

    def ResetIconImages(self):
        pass

    def SetConfigFile(self):
        pass

    def SetMacroButtonStates(self):
        pass


class CustomAttributeContainer(ReferenceTarget):
    thisown = ()

    def Append(self):
        pass

    def CanAccept(self):
        pass

    def FindInterface(self):
        pass

    def GetOwner(self):
        pass

    def Insert(self):
        pass

    def Remove(self):
        pass


class DimType:
    Angle = 0

    Color = 0

    Color255 = 0

    Custom = 0

    Dimensionless = 0

    Normalized = 0

    Percent = 0

    Segments = 0

    Time = 0

    World = 0

    thisown = ()



class DisplayFilters:
    GetCount = ()

    GetEnabled = ()

    GetHideFrozen = ()

    GetName = ()

    GetSceneDisplayFlag = ()

    IsNodeVisible = ()

    SetEnabled = ()

    SetSceneDisplayFlag = ()

    thisown = ()

    def GetCount(self):
        pass

    def GetEnabled(self):
        pass

    def GetHideFrozen(self):
        pass

    def GetName(self):
        pass

    def GetSceneDisplayFlag(self):
        pass

    def IsNodeVisible(self):
        pass

    def SetEnabled(self):
        pass

    def SetSceneDisplayFlag(self):
        pass


class DOFParams(Wrapper):
    thisown = ()
    def GetAxis(self):
        pass

    def GetCurVal(self):
        pass

    def GetDisplay(self):
        pass

    def GetEndEffector(self):
        pass

    def GetEndEffectorTM(self):
        pass

    def GetLimit(self):
        pass

    def GetMax(self):
        pass

    def GetMin(self):
        pass

    def GetNumDof(self):
        pass

    def GetPos(self):
        pass

    def GetSel(self):
        pass


class DoubleList:
    this = 0
    thisown = ()

    def Append(self):
        pass

    def Delete(self):
        pass

    def GetCount(self):
        pass

    def GetItem(self):
        pass

    def Insert(self):
        pass

    def SetCount(self):
        pass

    def SetItem(self):
        pass


class DWORDList:
    this = 0
    thisown = ()

    def Append(self):
        pass

    def Delete(self):
        pass

    def GetCount(self):
        pass

    def GetItem(self):
        pass

    def Insert(self):
        pass

    def SetCount(self):
        pass

    def SetItem(self):
        pass


class Effect(SpecialFX):
    thisown = ()
    def GBufferChannelsRequired(self):
        pass


class Effects:
    Add = ()

    CloseDialog = ()

    Delete = ()

    Edit = ()

    Get = ()

    GetCount = ()

    OpenDialog = ()

    Set = ()

    thisown = ()

    def Add(self):
        pass

    def CloseDialog(self):
        pass

    def Delete(self):
        pass

    def Edit(self):
        pass

    def Get(self):
        pass

    def GetCount(self):
        pass

    def OpenDialog(self):
        pass

    def Set(self):
        pass


class Environment:
    AddLightToScene = ()

    GetAmbient = ()

    GetAmbientController = ()

    GetLightConeConstraint = ()

    GetLightLevel = ()

    GetLightLevelController = ()

    GetLightTint = ()

    GetLightTintController = ()

    GetMap = ()

    GetMapEnabled = ()

    SetAmbient = ()

    SetAmbientController = ()

    SetLightLevel = ()

    SetLightLevelController = ()

    SetLightTint = ()

    SetLightTintController = ()

    SetMap = ()

    SetMapEnabled = ()

    thisown = ()

    def AddLightToScene(self):
        pass

    def GetAmbient(self):
        pass

    def GetAmbientController(self):
        pass

    def GetLightConeConstraint(self):
        pass

    def GetLightLevel(self):
        pass

    def GetLightLevelController(self):
        pass

    def GetLightTint(self):
        pass

    def GetLightTintController(self):
        pass

    def GetMap(self):
        pass

    def GetMapEnabled(self):
        pass

    def SetAmbient(self):
        pass

    def SetAmbientController(self):
        pass

    def SetLightLevel(self):
        pass

    def SetLightLevelController(self):
        pass

    def SetLightTint(self):
        pass

    def SetLightTintController(self):
        pass

    def SetMap(self):
        pass

    def SetMapEnabled(self):
        pass


class Face(Wrapper):
    thisown = ()
    def GetDirection(self):
        pass

    def GetEdgeIndex(self):
        pass

    def GetEdgeVis(self):
        pass

    def GetMatID(self):
        pass

    def GetOtherIndex(self):
        pass

    def GetSmGroup(self):
        pass

    def GetVert(self):
        pass

    def GetVertIndex(self):
        pass

    def Hide(self):
        pass

    def IsBackFacing(self):
        pass

    def IsHidden(self):
        pass

    def IsInForeground(self):
        pass

    def PushToBackground(self):
        pass

    def PushToForeground(self):
        pass

    def SetBackFacing(self):
        pass

    def SetEdgeVis(self):
        pass

    def SetEdgeVisFlags(self):
        pass

    def SetFrontFacing(self):
        pass

    def SetHide(self):
        pass

    def SetInForegound(self):
        pass

    def SetMatID(self):
        pass

    def SetSmGroup(self):
        pass

    def SetVerts(self):
        pass

    def Show(self):
        pass


class FacePoints:
    this = 0
    A = ()
    B = ()
    C = ()
    Center = ()
    Points = ()
    thisown = ()
    def GetCenter(self):
        pass



class Factory:
    CreateAnimatable = ()

    CreateAtmospheric = ()

    CreateBitmap = ()

    CreateBoxGizmoObject = ()

    CreateCamera = ()

    CreateCameraObject = ()

    CreateCylGizmoObject = ()

    CreateDefaultBitmapTex = ()

    CreateDefaultBoolController = ()

    CreateDefaultColorController = ()

    CreateDefaultCompositeTex = ()

    CreateDefaultFloatController = ()

    CreateDefaultFRGBAController = ()

    CreateDefaultMasterPointController = ()

    CreateDefaultMatrix3Controller = ()

    CreateDefaultMixTex = ()

    CreateDefaultMultiMtl = ()

    CreateDefaultPoint2Controller = ()

    CreateDefaultPoint3Controller = ()

    CreateDefaultPoint4Controller = ()

    CreateDefaultPositionController = ()

    CreateDefaultRotationController = ()

    CreateDefaultScaleController = ()

    CreateDefaultSoundObj = ()

    CreateDefaultStdCubic = ()

    CreateDefaultStdFog = ()

    CreateDefaultStdMat = ()

    CreateDefaultStdMirror = ()

    CreateDefaultTintTex = ()

    CreateDerivedObject = ()

    CreateDirectionalLight = ()

    CreateDummyObject = ()

    CreateFloatController = ()

    CreateFreeCamera = ()

    CreateGeomObject = ()

    CreateGizmoObject = ()

    CreateHelperObject = ()

    CreateInterpFloat = ()

    CreateInterpPoint2 = ()

    CreateInterpPoint3 = ()

    CreateInterpPoint4 = ()

    CreateInterpPosition = ()

    CreateInterpRotation = ()

    CreateInterpScale = ()

    CreateLight = ()

    CreateLightObject = ()

    CreateLookatControl = ()

    CreateMasterPointControl = ()

    CreateMaterial = ()

    CreateMatrix3Controller = ()

    CreateMorphController = ()

    CreateNewMesh = ()

    CreateNewTriObject = ()

    CreateNode = ()

    CreateObject = ()

    CreateObjectModifier = ()

    CreateOmniLight = ()

    CreateParallelCamera = ()

    CreatePoint3Controller = ()

    CreatePositionController = ()

    CreatePRSControl = ()

    CreateRenderElement = ()

    CreateRenderer = ()

    CreateRenderingEffect = ()

    CreateRotationController = ()

    CreateScaleController = ()

    CreateShapeObject = ()

    CreateSound = ()

    CreateSphereGizmoObject = ()

    CreateStorage = ()

    CreateTargetedCamera = ()

    CreateTargetedDirectionalLight = ()

    CreateTargetedSpotLight = ()

    CreateTargetObject = ()

    CreateTextureMap = ()

    CreateWorldSpaceModifier = ()

    CreateWSDerivedObject = ()

    GetDefaultController = ()

    IsCreatingObject = ()

    SetDefaultBoolController = ()

    SetDefaultColorController = ()

    SetDefaultController = ()

    SetDefaultFRGBAController = ()

    StartCreatingObject = ()

    StopCreating = ()

    def CreateAnimatable(self, SClass_ID, Class_ID, bool):
        return Animatable()

    def CreateAtmospheric(self, Class_ID):
        return Atmospheric()

    def CreateBitmap(self, BitmapInfo):
        return Bitmap()

    def CreateBoxGizmoObject(self):
        return GizmoObject()

    def CreateCamera(self, Class_ID):
        return CameraObject()

    def CreateCameraObject(self, int):
        return GenCamera()

    def CreateCylGizmoObject(self):
        return GizmoObject()

    def CreateDefaultBitmapTex(self):
        return BitmapTex()

    def CreateDefaultBoolController(self):
        return Control()

    def CreateDefaultColorController(self):
        return Control()

    def CreateDefaultCompositeTex(self):
        return Texmap()

    def CreateDefaultFloatController(self):
        return Control()

    def CreateDefaultFRGBAController(self):
        return Control()

    def CreateDefaultMasterPointController(self):
        return Control()

    def CreateDefaultMatrix3Controller(self):
        return Control()

    def CreateDefaultMixTex(self):
        return Texmap()

    def CreateDefaultMultiMtl(self):
        return MultiMtl()

    def CreateDefaultPoint2Controller(self):
        return Control()

    def CreateDefaultPoint3Controller(self):
        return Control()

    def CreateDefaultPoint4Controller(self):
        return Control()

    def CreateDefaultPositionController(self):
        return Control()

    def CreateDefaultRotationController(self):
        return Control()

    def CreateDefaultScaleController(self):
        return Control()

    def CreateDefaultSoundObj(self):
        return SoundObj()

    def CreateDefaultStdCubic(self):
        return Texmap()

    def CreateDefaultStdFog(self):
        return Atmospheric()

    def CreateDefaultStdMat(self):
        return StdMat()

    def CreateDefaultStdMirror(self):
        return Texmap()

    def CreateDefaultTintTex(self):
        return Texmap()

    def CreateDerivedObject(self):
        return IDerivedObject()

    def CreateDirectionalLight(self):
        return GenLight()

    def CreateDummyObject(self):
        return DummyObject()

    def CreateFloatController(self, Class_ID):
        return Control()

    def CreateFreeCamera(self):
        return GenCamera()

    def CreateGeomObject(self, Class_ID):
        return GeomObject()

    def CreateGizmoObject(self, Class_ID):
        return GizmoObject()

    def CreateHelperObject(self, Class_ID):
        return HelperObject()

    def CreateInterpFloat(self):
        return Control()

    def CreateInterpPoint2(self):
        return Control()

    def CreateInterpPoint3(self):
        return Control()

    def CreateInterpPoint4(self):
        return Control()

    def CreateInterpPosition(self):
        return Control()

    def CreateInterpRotation(self):
        return Control()

    def CreateInterpScale(self):
        return Control()

    def CreateLight(self, Class_ID):
        return LightObject()

    def CreateLightObject(self, int):
        return GenLight()

    def CreateLookatControl(self):
        return Control()

    def CreateMasterPointControl(self):
        return Control()

    def CreateMaterial(self, Class_ID):
        return Mtl()

    def CreateMatrix3Controller(self, Class_ID):
        return Control()

    def CreateMorphController(self, Class_ID):
        return Control()

    def CreateNewMesh(self):
        return Mesh()

    def CreateNewTriObject(self):
        return TriObject()

    def CreateNode(self, Object):
        return INode()

    def CreateObject(self, SClass_ID, Class_ID):
        return Object()

    def CreateObjectModifier(self, Class_ID):
        return Modifier()

    def CreateOmniLight(self):
        return GenLight()

    def CreateParallelCamera(self):
        return GenCamera()

    def CreatePoint3Controller(self, Class_ID):
        return Control()

    def CreatePositionController(self, Class_ID):
        return Control()

    def CreatePRSControl(self):
        return Control()

    def CreateRenderElement(self, Class_ID):
        return RenderElement()

    def CreateRenderer(self, Class_ID):
        return Renderer()

    def CreateRenderingEffect(self, Class_ID):
        return Effect()

    def CreateRotationController(self, Class_ID):
        return Control()

    def CreateScaleController(self, Class_ID):
        return Control()

    def CreateShapeObject(self, Class_ID):
        return ShapeObject()

    def CreateSound(self, Class_ID):
        return SoundObj()

    def CreateSphereGizmoObject(self):
        return GizmoObject()

    def CreateStorage(self,UINT):
        return BitmapStorage()

    def CreateTargetedCamera(self):
        return GenCamera()

    def CreateTargetedDirectionalLight(self, INode):
        return GenLight()

    def CreateTargetedSpotLight(self):
        return GenLight()

    def CreateTargetObject(self):
        return Object()

    def CreateTextureMap(self, Class_ID):
        return Texmap()

    def CreateWorldSpaceModifier(self, Class_ID):
        return Modifier()

    def CreateWSDerivedObject(self, Object):
        return IDerivedObject()

    def GetDefaultController(self, SClass_ID):
        return ClassDesc()

    def IsCreatingObject(self, Class_ID):
        pass

    def SetDefaultBoolController(self, ClassDesc):
        pass

    def SetDefaultColorController(self,ClassDesc):
        pass

    def SetDefaultController(self, SClass_ID, ClassDesc):
        pass

    def SetDefaultFRGBAController(self, ClassDesc):
        pass

    def StartCreatingObject(self, ClassDesc):
        pass

    def StopCreating(self):
        pass


class FileManager:
    AppendToCurFilePath = ()
    CanImportBitmap = ()
    CanImportFile = ()
    CheckForSave = ()
    ChooseDirectory = ()
    ConfigureBitmapPaths = ()
    DoesFileExist = ()
    DoMaxFileSaveAsDlg = ()
    DownloadUrl = ()
    Export = ()
    ExportSelected = ()
    Fetch = ()
    GetFileName = ()
    GetFileNameAndPath = ()
    GetSaveRequiredFlag = ()
    GetSavingVersion = ()
    Hold = ()
    Import = ()
    IsAutoSaveRequired = ()
    IsInternetCachedFile = ()
    IsMaxFile = ()
    IsSaveRequired = ()
    IsSavingToFile = ()
    Merge = ()
    Open = ()
    Reset = ()
    Save = ()
    SaveAs = ()
    SaveNodes = ()
    SaveNodesAsVersion = ()
    SaveSceneAsVersion = ()
    SaveSelected = ()
    SaveSelectedNodesAsVersion = ()
    SetSaveRequiredFlag = ()
    SetSavingVersion = ()
    thisown = ()
    def AppendToCurFilePath(self, string):
        pass

    def CanImportBitmap(self,filename):
        pass

    def CanImportFile(self,filename):
        pass

    def CheckForSave(self):
        pass

    def ChooseDirectory(self, HWND, title, dir, desc):
        pass

    def ConfigureBitmapPaths(self):
        pass

    def DoesFileExist(self, filename, bool):
        pass

    def DoMaxFileSaveAsDlg(self, filename, bool):
        pass

    def DownloadUrl(self, HWND, url, filename, DWORD):
        pass

    def Export(self, name, bool):
        pass

    def ExportSelected(self, name, bool):
        pass

    def Fetch(self):
        pass

    def GetFileName(self):
        return WStr()

    def GetFileNameAndPath(self):
        return WStr()

    def GetSaveRequiredFlag(self):
        return True

    def GetSavingVersion(self):
        return DWORD()

    def Hold(self):
        pass

    def Import(self, name, bool):
        pass

    def IsAutoSaveRequired(self):
        pass

    def IsInternetCachedFile(self,filename):
        return True

    def IsMaxFile(self, filename):
        pass

    def IsSaveRequired(self):
        pass

    def IsSavingToFile(self):
        pass

    def Merge(self, name, isMergeAll, bool):
        pass

    def Open(self, name):
        pass

    def Reset(self):
        pass

    def Save(self, name):
        pass

    def SaveAs(self):
        pass

    def SaveNodes(self, INodeTab, fname):
        pass

    def SaveNodesAsVersion(self, fname, INodeTab):
        pass

    def SaveSceneAsVersion(self, fname):
        pass

    def SaveSelected(self, fname):
        pass

    def SaveSelectedNodesAsVersion(self, fname):
        pass

    def SetSaveRequiredFlag(self):
        pass

    def SetSavingVersion(self, DWORD):
        pass


class FilterKernel(SpecialFX):
    thisown = ()
    def GetDefaultComment(self):
        pass

    def GetFilterParam(self):
        pass

    def GetFilterParamMax(self):
        pass

    def GetFilterParamName(self):
        pass

    def GetKernelSupport(self):
        pass

    def GetKernelSupportY(self):
        pass

    def GetKernelSzX(self):
        pass

    def GetKernelSzY(self):
        pass

    def GetNumFilterParams(self):
        pass

    def HasNegativeLobes(self):
        pass

    def Is2DKernel(self):
        pass

    def IsNormalized(self):
        pass

    def IsVariableSz(self):
        pass

    def SetFilterParam(self):
        pass

    def SetKernelSz(self):
        pass


class FloatList:
    this = 0
    thisown = ()

    def Append(self):
        pass

    def Delete(self):
        pass

    def GetCount(self):
        pass

    def GetItem(self):
        pass

    def Insert(self):
        pass

    def SetCount(self):
        pass

    def SetItem(self):
        pass


class FPInterfaceDesc(FPInterface):
    thisown = ()

    def EnableActions(self):
        pass

    def GetActionTable(self):
        pass

    def GetClassDesc(self):
        pass

    def GetDescription(self):
        pass

    def GetFlags(self):
        pass

    def GetFPDesc(self):
        pass

    def GetID(self):
        pass

    def GetInterface(self):
        pass

    def GetInternalName(self):
        pass

    def GetRsrcString(self):
        pass


class FPInterfaceList:
    this = 0
    thisown = ()

    def Append(self):
        pass

    def Delete(self):
        pass

    def GetCount(self):
        pass

    def GetItem(self):
        pass

    def Insert(self):
        pass

    def SetCount(self):
        pass

    def SetItem(self):
        pass


class FPStaticInterface(FPInterfaceDesc):
    thisown = ()


class FPTypeConstants:
    AngAxis = 0
    AngAxisTab = 0
    Angle = 0
    AngleTab = 0
    BitArray = 0
    BitArrayTab = 0
    Bitmap = 0
    BitmapTab = 0
    BOOL = 0
    Bool = 0
    BOOLTab = 0
    BoolTab = 0
    ClassDesc = 0
    ClassDescTab = 0
    Color = 0
    ColorChannel = 0
    ColorChannelTab = 0
    ColorTab = 0
    Control = 0
    ControlTab = 0
    Double = 0
    DoubleTab = 0
    DWORD = 0
    DWORDTab = 0
    Enum = 0
    EnumTab = 0
    FileName = 0
    FileNameTab = 0
    Float = 0
    FloatTab = 0
    FPInterface = 0
    FPInterfaceTab = 0
    FPValue = 0
    FPValueTab = 0
    FRgb = 0
    FRgbTab = 0
    Hsv = 0
    HsvTab = 0
    HWND = 0
    HWNDTab = 0
    Index = 0
    IndexTab = 0
    Int = 0
    Int64 = 0
    Int64Tab = 0
    Interval = 0
    IntervalTab = 0
    IntPtr = 0
    IntPtrTab = 0
    IntTab = 0
    IObject = 0
    IObjectTab = 0
    Matrix3 = 0
    Matrix3Tab = 0
    Mesh = 0
    MeshTab = 0
    MSFloat = 0
    Mtl = 0
    MtlTab = 0
    Name = 0
    NameTab = 0
    Node = 0
    NodeTab = 0
    Object = 0
    ObjectTab = 0
    PBlock2 = 0
    PBlock2Tab = 0
    PercentFraction = 0
    PercentFractionTab = 0
    Point = 0
    Point2 = 0
    Point2Tab = 0
    Point3 = 0
    Point3Tab = 0
    Point4 = 0
    Point4Tab = 0
    PointTab = 0
    Quat = 0
    QuatTab = 0
    RadioButtonIndex = 0
    RadioButtonIndexTab = 0
    Ray = 0
    RayTab = 0
    RefTarg = 0
    RefTargTab = 0
    Rgb = 0
    RgbTab = 0
    Str = 0
    String = 0
    StringTab = 0
    StrTab = 0
    Texmap = 0
    TexmapTab = 0
    TimeValue = 0
    TimeValueTab = 0
    Value = 0
    ValueTab = 0
    Void = 0
    VoidTab = 0
    World = 0
    WorldTab = 0
    thisown = ()


class FPValue(Wrapper):
    this = ()
    def Free(self):
        pass

    def GetAColor(self):
        pass

    def GetAColorList(self):
        pass

    def GetAngAxis(self):
        pass

    def GetAngAxisList(self):
        pass

    def GetBitArray(self):
        pass

    def GetBitArrayList(self):
        pass

    def GetBitmap(self):
        pass

    def GetBitmapList(self):
        pass

    def GetBool(self):
        pass

    def GetBoolList(self):
        pass

    def GetClassDesc(self):
        pass

    def GetClassDescList(self):
        pass

    def GetColor(self):
        pass

    def GetColorList(self):
        pass

    def GetControl(self):
        pass

    def GetControlList(self):
        pass

    def GetDouble(self):
        pass

    def GetDoubleList(self):
        pass

    def GetDWORD(self):
        pass

    def GetDWORDList(self):
        pass

    def GetFloat(self):
        pass

    def GetFloatList(self):
        pass

    def GetFPInterface(self):
        pass

    def GetFPInterfaceList(self):
        pass

    def GetInt(self):
        pass

    def GetInt64(self):
        pass

    def GetInt64List(self):
        pass

    def GetInterval(self):
        pass

    def GetIntervalList(self):
        pass

    def GetIntList(self):
        pass

    def GetIObject(self):
        pass

    def GetIObjectList(self):
        pass

    def GetIParamBlock2(self):
        pass

    def GetIParamBlock2List(self):
        pass

    def GetIPoint2(self):
        return IPoint2()

    def GetIPoint2List(self):
        pass

    def GetMatrix3(self):
        pass

    def GetMatrix3List(self):
        pass

    def GetMesh(self):
        pass

    def GetMeshList(self):
        pass

    def GetMtl(self):
        pass

    def GetMtlList(self):
        pass

    def GetNode(self):
        pass

    def GetNodeList(self):
        pass

    def GetObject(self):
        pass

    def GetObjectList(self):
        pass

    def GetParamDimension(self):
        pass

    def GetPChar(self):
        pass

    def GetPCharList(self):
        pass

    def GetPoint2(self):
        pass

    def GetPoint2List(self):
        pass

    def GetPoint3(self):
        pass

    def GetPoint3List(self):
        pass

    def GetPoint4(self):
        pass

    def GetPoint4List(self):
        pass

    def GetQuat(self):
        pass

    def GetQuatList(self):
        pass

    def GetRay(self):
        pass

    def GetRayList(self):
        pass

    def GetReferenceTarget(self):
        pass

    def GetReferenceTargetList(self):
        pass

    def GetStr(self):
        pass

    def GetStrList(self):
        pass

    def GetTexmap(self):
        pass

    def GetTexmapList(self):
        pass

    def GetType(self):
        pass

    def Init(self):
        pass

    def InitTab(self):
        pass

    def IsPointerBasedType(self):
        pass

    def IsTabType(self):
        pass

    def Set(self):
        pass

    def SetType(self):
        pass


class GammaMgr:
    DeGammaCorrect = ()

    DisplayGammaCorrect = ()

    Enable = ()

    GammaCorrect = ()

    GetDisplayGamma = ()

    GetDitherPaletted = ()

    GetDitherTrue = ()

    GetFileInGamma = ()

    GetFileOutGamma = ()

    IsEnabled = ()

    SetDisplayGamma = ()

    SetDitherPaletted = ()

    SetDitherTrue = ()

    SetFileInGamma = ()

    SetFileOutGamma = ()

    thisown = ()

    def DeGammaCorrect(self):
        pass

    def DisplayGammaCorrect(self):
        pass

    def Enable(self):
        pass

    def GammaCorrect(self):
        pass

    def GetDisplayGamma(self):
        pass

    def GetDitherPaletted(self):
        pass

    def GetDitherTrue(self):
        pass

    def GetFileInGamma(self):
        pass

    def GetFileOutGamma(self):
        pass

    def IsEnabled(self):
        pass

    def SetDisplayGamma(self):
        pass

    def SetDitherPaletted(self):
        pass

    def SetDitherTrue(self):
        pass

    def SetFileInGamma(self):
        pass

    def SetFileOutGamma(self):
        pass


class Grid:
    Add = ()

    GetActive = ()

    GetIntensity = ()

    GetMajorLines = ()

    GetSpacing = ()

    GetUseGridColor = ()

    GetWhiteOrigin = ()

    SetActive = ()

    SetIntensity = ()

    SetMajorLines = ()

    SetSpacing = ()

    SetUseGridColor = ()

    SetWhiteOrigin = ()

    thisown = ()

    def Add(self):
        pass

    def GetActive(self):
        pass

    def GetIntensity(self):
        pass

    def GetMajorLines(self):
        pass

    def GetSpacing(self):
        pass

    def GetUseGridColor(self):
        pass

    def GetWhiteOrigin(self):
        pass

    def SetActive(self):
        pass

    def SetIntensity(self):
        pass

    def SetMajorLines(self):
        pass

    def SetSpacing(self):
        pass

    def SetUseGridColor(self):
        pass

    def SetWhiteOrigin(self):
        pass


class HDRColor(Wrapper):
    this = ()
    def ClipColor(self):
        pass

    def GetA(self):
        pass

    def GetB(self):
        pass

    def GetG(self):
        pass

    def GetR(self):
        pass

    def SetA(self):
        pass

    def SetB(self):
        pass

    def SetG(self):
        pass

    def SetR(self):
        pass


class INodeList:
    this = 0
    thisown = ()

    def Append(self):
        pass

    def Delete(self):
        pass

    def GetCount(self):
        pass

    def GetItem(self):
        pass

    def Insert(self):
        pass

    def SetCount(self):
        pass

    def SetItem(self):
        pass


class INodeTab:
    this = 0
    thisown = ()

    def Append(self):
        pass

    def GetCount(self):
        pass

    def GetItem(self):
        pass

    def IndexOf(self):
        pass

    def Insert(self):
        pass

    def Remove(self):
        pass


class Int64List:
    this = 0
    thisown = ()

    def Append(self):
        pass

    def Delete(self):
        pass

    def GetCount(self):
        pass

    def GetItem(self):
        pass

    def Insert(self):
        pass

    def SetCount(self):
        pass

    def SetItem(self):
        pass


class Interface_ID(Wrapper):
    this = ()
    def GetPartA(self):
        pass

    def GetPartB(self):
        pass

    def SetPartA(self):
        pass

    def SetPartB(self):
        pass


class InterfaceIds:
    thisown = ()



class Interval(Wrapper):
    this = ()
    def Duration(self):
        return TimeValue()

    def Empty(self):
        return True

    def End(self):
        return TimeValue()

    def InInterval(self, TimeValue):
        return True

    def Set(self, start, end):
        pass

    def SetEmpty(self):
        pass

    def SetEnd(self, TimeValue):
        pass

    def SetInfinite(self):
        pass

    def SetInstant(self, TimeValue):
        pass

    def SetStart(self, TimeValue):
        pass

    def Start(self):
        pass


class IntervalList:
    this = 0
    thisown = ()

    def Append(self):
        pass

    def Delete(self):
        pass

    def GetCount(self):
        pass

    def GetItem(self):
        pass

    def Insert(self):
        pass

    def SetCount(self):
        pass

    def SetItem(self):
        pass


class IntList:
    this = 0
    thisown = ()

    def Append(self):
        pass

    def Delete(self):
        pass

    def GetCount(self):
        pass

    def GetItem(self):
        pass

    def Insert(self):
        pass

    def SetCount(self):
        pass

    def SetItem(self):
        pass


class IObjectList:
    this = 0
    thisown = ()

    def Append(self):
        pass

    def Delete(self):
        pass

    def GetCount(self):
        pass

    def GetItem(self):
        pass

    def Insert(self):
        pass

    def SetCount(self):
        pass

    def SetItem(self):
        pass


class IParamArray(Wrapper):
    thisown = ()
    def GetParamBlock(self):
        return IParamBlock()

    def GetValue(self, int, TimeValue, float, Interval):
        return True

    def KeyFrameAtTime(self, int, TimeValue):
        return True

    def SetValue(self, int, TimeValue, float):
        return True


class IParamBlock2List:
    this = 0
    thisown = ()

    def Append(self, IParamBlock2):
        pass

    def Delete(self, int):
        pass

    def GetCount(self):
        return 0

    def GetItem(self, int):
        return IParamBlock2()

    def Insert(self, IParamBlock2, int):
        pass

    def SetCount(self, int):
        pass

    def SetItem(self, int, IParamBlock2):
        pass


class IParamMap(Wrapper):
    thisown = ()
    def GetParamArray(self):
        return IParamArray()
    def Invalidate(self):
        pass


class IPoint2(Wrapper):
    this = ()
    X = ()
    Y = ()
    def DotProd(self, IPoint2):
        return 0

    def GetLength(self):
        return 0.0

    def GetMaxComponent(self):
        return 0

    def GetMinComponent(self):
        return 0

    def GetX(self):
        return 0

    def GetY(self):
        return 0

    def SetX(self, int):
        pass

    def SetY(self, int):
        pass


class IPoint2List:
    this = ()
    def Append(self, IPoint2):
        pass

    def Delete(self, int):
        pass

    def GetCount(self):
        pass

    def GetItem(self, int):
        return IPoint2()

    def Insert(self):
        pass

    def SetCount(self):
        pass

    def SetItem(self):
        pass


class IPoint3(Wrapper):
    this = ()

    def CrossProd(self, IPoint3):
        return IPoint3()

    def DotProd(self, IPoint3):
        return 0

    def GetLength(self):
        return 0.0

    def GetMaxComponent(self):
        return 0

    def GetMinComponent(self):
        return 0

    def GetX(self):
        return 0

    def GetY(self):
        return 0

    def GetZ(self):
        return 0

    def SetX(self, int):
        pass

    def SetY(self, int):
        pass

    def SetZ(self, int):
        pass


class IScanRenderer(Renderer):
    thisown = ()

    def GetAntialias(self):
        pass

    def GetAntiAliasFilter(self):
        pass

    def GetAntiAliasFilterSz(self):
        pass

    def GetApplyVelBlurEnv(self):
        pass

    def GetAutoReflect(self):
        pass

    def GetAutoReflLevels(self):
        pass

    def GetColorClampType(self):
        pass

    def GetDesc(self):
        pass

    def GetFilter(self):
        pass

    def GetForceWire(self):
        pass

    def GetGlobalSamplerAdaptive(self):
        pass

    def GetGlobalSamplerAdaptiveThresh(self):
        pass

    def GetGlobalSamplerClassByName(self):
        pass

    def GetGlobalSamplerEnabled(self):
        pass

    def GetGlobalSamplerParam1(self):
        pass

    def GetGlobalSamplerParam2(self):
        pass

    def GetGlobalSamplerQuality(self):
        pass

    def GetGlobalSamplerSampleMaps(self):
        pass

    def GetMapping(self):
        pass

    def GetMaxRayDepth(self):
        pass

    def GetMemFrugal(self):
        pass

    def GetNBlurFrames(self):
        pass

    def GetNBlurSamples(self):
        pass

    def GetObjBlurDuration(self):
        pass

    def GetObjMotBlur(self):
        pass

    def GetPixelSamplerEnable(self):
        pass

    def GetShadows(self):
        pass

    def GetVelBlurDuration(self):
        pass

    def GetVelBlurTrans(self):
        pass

    def GetVelMotBlur(self):
        pass

    def GetWireThickness(self):
        pass

    def IsSSEEnabled(self):
        pass

    def SetAntialias(self):
        pass

    def SetAntiAliasFilter(self):
        pass

    def SetAntiAliasFilterRT(self):
        pass

    def SetAntiAliasFilterSz(self):
        pass

    def SetApplyVelBlurEnv(self):
        pass

    def SetAutoReflect(self):
        pass

    def SetAutoReflLevels(self):
        pass

    def SetColorClampType(self):
        pass

    def SetEnableSSE(self):
        pass

    def SetFilter(self):
        pass

    def SetForceWire(self):
        pass

    def SetGlobalSamplerAdaptive(self):
        pass

    def SetGlobalSamplerAdaptiveThresh(self):
        pass

    def SetGlobalSamplerClassByName(self):
        pass

    def SetGlobalSamplerEnabled(self):
        pass

    def SetGlobalSamplerParam1(self):
        pass

    def SetGlobalSamplerParam2(self):
        pass

    def SetGlobalSamplerQuality(self):
        pass

    def SetGlobalSamplerSampleMaps(self):
        pass

    def SetMapping(self):
        pass

    def SetMaxRayDepth(self):
        pass

    def SetMemFrugal(self):
        pass

    def SetNBlurFrames(self):
        pass

    def SetNBlurSamples(self):
        pass

    def SetObjBlurDuration(self):
        pass

    def SetObjMotBlur(self):
        pass

    def SetPixelSamplerEnable(self):
        pass

    def SetPixelSize(self):
        pass

    def SetShadows(self):
        pass

    def SetVelBlurDuration(self):
        pass

    def SetVelBlurTrans(self):
        pass

    def SetVelMotBlur(self):
        pass

    def SetWireThickness(self):
        pass


class ISubMap(Wrapper):
    thisown = ()
    def GetMapSlotType(self):
        pass

    def GetNumSubTexmaps(self):
        pass

    def GetRefTarget(self):
        pass

    def GetSubTexmap(self):
        pass

    def GetSubTexmapSlotName(self):
        pass

    def GetSubTexmapTVName(self):
        pass

    def IsSubTexmapOn(self):
        pass

    def SetSubTexmap(self):
        pass


class LayerManager:
    AddLayer = ()

    CreateLayer = ()

    DeleteLayer = ()

    DoLayerPropDialog = ()

    EditLayer = ()

    GetCurrentLayer = ()

    GetLayer = ()

    GetNumLayers = ()

    GetPropagateToLayer = ()

    GetRootLayer = ()

    GetSavedLayer = ()

    Reset = ()

    SetCurrentLayer = ()

    SetPropagateToLayer = ()

    thisown = ()

    def AddLayer(self):
        pass

    def CreateLayer(self):
        pass

    def DeleteLayer(self):
        pass

    def DoLayerPropDialog(self):
        pass

    def EditLayer(self):
        pass

    def GetCurrentLayer(self):
        pass

    def GetLayer(self):
        pass

    def GetNumLayers(self):
        pass

    def GetPropagateToLayer(self):
        pass

    def GetRootLayer(self):
        pass

    def GetSavedLayer(self):
        pass

    def Reset(self):
        pass

    def SetCurrentLayer(self):
        pass

    def SetPropagateToLayer(self):
        pass


class LightState(Wrapper):
    this = 0
    thisown = ()
    def GetAffectDiffuse(self):
        pass

    def GetAffectSpecular(self):
        pass

    def GetAmbientOnly(self):
        pass

    def GetAspect(self):
        pass

    def GetAttenuationEnd(self):
        pass

    def GetAttenuationStart(self):
        pass

    def GetColor(self):
        pass

    def GetExtra(self):
        pass

    def GetFallSize(self):
        pass

    def GetHotSize(self):
        pass

    def GetIntensity(self):
        pass

    def GetNearAttenEnd(self):
        pass

    def GetNearAttenStart(self):
        pass

    def GetOn(self):
        pass

    def GetOvershoot(self):
        pass

    def GetShadow(self):
        pass

    def GetShape(self):
        pass

    def GetTM(self):
        pass

    def GetType(self):
        pass

    def GetUseAtten(self):
        pass

    def GetUseNearAtten(self):
        pass


class LinearShape(ShapeObject):
    thisown = ()

    def CopyFrom(self):
        pass

    def GetShape(self):
        pass


class MappingChannel:
    ChannelId = ()

    Enabled = ()

    NumFaces = ()

    NumTextureVertices = ()

    TextureFaces = ()

    TextureFaceVertices = ()

    TextureVertices = ()

    thisown = ()

    def GetChannelId(self):
        pass

    def GetNumFaces(self):
        pass

    def GetNumTextureVertices(self):
        pass

    def GetTextureFace(self):
        pass

    def GetTextureFaceVertex(self):
        pass

    def GetTextureFaceVertices(self):
        pass

    def GetTextureVertex(self):
        pass

    def IsEnabled(self):
        pass

    def SetEnabled(self):
        pass

    def SetNumTextureVertices(self):
        pass

    def SetTextureFace(self):
        pass

    def SetTextureVertex(self):
        pass



class MaterialEditor:
    CloseMtlDlg = ()
    FindMtlNameInScene = ()
    FlushMtlDlg = ()
    GetActiveSlot = ()
    GetMtlDlgMode = ()
    GetNumSlots = ()
    IsMtlDlgShowing = ()
    IsMtlInstanced = ()
    LoadMaterialLibrary = ()
    OpenMtlDlg = ()
    PutMaterial = ()
    SaveMaterialLibrary = ()
    SetActiveSlot = ()
    SetMtlDlgMode = ()
    SetSlot = ()
    thisown = ()
    UnFlushMtlDlg = ()
    UpdateMtlEditorBrackets = ()

    def CloseMtlDlg(self, int):
        pass

    def FindMtlNameInScene(self, WStr):
        return Mtl()

    def FlushMtlDlg(self):
        pass

    def GetActiveSlot(self):
        return 0

    def GetMtlDlgMode(self):
        return 0

    def GetNumSlots(self):
        return 0

    def IsMtlDlgShowing(self, int):
        return True

    def IsMtlInstanced(self, MtlBase):
        return True

    def LoadMaterialLibrary(self, name):
        return 0

    def OpenMtlDlg(self, int):
        pass

    def PutMaterial(self, MtlBase, oldMtl):
        pass

    def SaveMaterialLibrary(self, name):
        pass

    def SetActiveSlot(self, int):
        pass

    def SetMtlDlgMode(self, int):
        pass

    def SetSlot(self, int, MtlBase):
        pass

    def UnFlushMtlDlg(self):
        pass

    def UpdateMtlEditorBrackets(self):
        pass



class MaterialManager:
    DoMaterialBrowseDlg = ()
    GetMatLibFileName = ()
    GetMtlSlot = ()
    IsMtlOkForScene = ()
    PutMtlToMtlEditor = ()
    thisown = ()

    def DoMaterialBrowseDlg(self, HWND, DWORD, int, int):
        return MtlBase()

    def GetMatLibFileName(self):
        return ''

    def GetMtlSlot(self):
        return MtlBase()

    def IsMtlOkForScene(self, MtlBase):
        return True

    def PutMtlToMtlEditor(self, MtlBase):
        pass


class Math:
    BasisFromZDir = ()

    Bias = ()

    BoxStep = ()

    Clamp = ()

    Gain = ()

    Noise1 = ()

    Noise2 = ()

    Noise3 = ()

    Noise3DS = ()

    Noise4 = ()

    SmoothStep = ()

    SRamp = ()

    thisown = ()

    Threshold = ()

    Turbulence = ()

    def BasisFromZDir(self):
        pass

    def Bias(self):
        pass

    def BoxStep(self):
        pass

    def Clamp(self):
        pass

    def Gain(self):
        pass

    def Noise1(self):
        pass

    def Noise2(self):
        pass

    def Noise3(self):
        pass

    def Noise3DS(self):
        pass

    def Noise4(self):
        pass

    def SmoothStep(self):
        pass

    def SRamp(self):
        pass

    def Threshold(self):
        pass

    def Turbulence(self):
        pass


class Matrix3(Wrapper):
    Columns = ()

    GetIdentity = ()

    Rotation = ()

    Rows = ()

    Scale = ()

    Translation = ()

    def Equals(self):
        pass

    def GetColumn(self):
        pass

    def GetColumn3(self):
        pass

    def GetIdentity(self):
        pass

    def GetNumColumns(self):
        pass

    def GetNumRows(self):
        pass

    def GetParity(self):
        pass

    def GetPitch(self):
        pass

    def GetRoll(self):
        pass

    def GetRotation(self):
        pass

    def GetRow(self):
        pass

    def GetScale(self):
        pass

    def GetTranslation(self):
        pass

    def GetYaw(self):
        pass

    def Invert(self):
        pass

    def IsIdentity(self):
        pass

    def NoRot(self):
        pass

    def NoScale(self):
        pass

    def NoTrans(self):
        pass

    def Orthogonalize(self):
        pass

    def PointTransform(self):
        pass

    def PreRotate(self):
        pass

    def PreRotateX(self):
        pass

    def PreRotateY(self):
        pass

    def PreRotateZ(self):
        pass

    def PreScale(self):
        pass

    def PreTranslate(self):
        pass

    def Rotate(self):
        pass

    def RotateX(self):
        pass

    def RotateY(self):
        pass

    def RotateZ(self):
        pass

    def Scale(self):
        pass

    def Set(self):
        pass

    def SetAngleAxis(self):
        pass

    def SetColumn(self):
        pass

    def SetFromToUp(self):
        pass

    def SetRotateX(self):
        pass

    def SetRotateY(self):
        pass

    def SetRotateZ(self):
        pass

    def SetRotation(self):
        pass

    def SetRow(self):
        pass

    def SetScale(self):
        pass

    def SetToRotation(self):
        pass

    def SetToScale(self):
        pass

    def SetTranslate(self):
        pass

    def SetTranslation(self):
        pass

    def ToIdentity(self):
        pass

    def Translate(self):
        pass

    def ValidateFlags(self):
        pass

    def VectorTransform(self):
        pass

    def Zero(self):
        pass


class Matrix3List:
    this = 0
    thisown = ()

    def Append(self):
        pass

    def Delete(self):
        pass

    def GetCount(self):
        pass

    def GetItem(self):
        pass

    def Insert(self):
        pass

    def SetCount(self):
        pass

    def SetItem(self):
        pass



class Menu(MenuElement):
    Items = ()
    NumItems = ()
    thisown = ()

    def GetItem(self, int):
        return MenuItem()

    def GetNumItems(self):
        return 0


class MenuBuilder:
    this = 0
    thisown = ()

    def AddItem(self, ActionItem):
        pass

    def AddSeparator(self):
        pass

    def AddSubMenu(self, Menu):
        pass

    def Create(self, Menu):
        pass


class MenuElement(Wrapper):
    IsEnabled = ()
    IsVisible = ()
    Title = ()

    def GetIsEnabled(self):
        return True
    def GetIsVisible(self):
        return True
    def GetTitle(self):
        return WStr()


class MenuItem(MenuElement):
    ActionItem = ()
    HasSubMenu = ()
    IsSeparator = ()
    SubMenu = ()
    thisown = ()

    def AsFPInterface(self):
        return FPInterface()

    def ExecuteAction(self):
        return True

    def GetActionItem(self):
        return ActionItem()

    def GetHasSubMenu(self):
        return True

    def GetIsSeparator(self):
        return True

    def GetSubMenu(self):
        return Menu()


class MenuManager(FPStaticInterface):
    FindMenu = ()
    GetMainMenu = ()
    GetMenuFile = ()
    LoadMenuFile = ()
    MenuExists = ()
    SaveMenuFile = ()
    thisown = ()
    UnregisterMenu = ()

    def FindMenu(self, name):
        return Menu()

    def GetMainMenu(self):
        return Menu()

    def GetMenuFile(self):
        return ''

    def LoadMenuFile(self, string):
        return True

    def MenuExists(self, name):
        return True

    def SaveMenuFile(self, string):
        return True

    def UnregisterMenu(self, name):
        pass


class MeshList:
    this = 0
    thisown = ()

    def Append(self):
        pass

    def Delete(self):
        pass

    def GetCount(self):
        pass

    def GetItem(self):
        pass

    def Insert(self):
        pass

    def SetCount(self):
        pass

    def SetItem(self):
        pass


class ModContextList:
    this = 0
    thisown = ()

    def Append(self):
        pass

    def Delete(self):
        pass

    def GetCount(self):
        pass

    def GetItem(self):
        pass

    def Insert(self):
        pass

    def SetCount(self):
        pass

    def SetItem(self):
        pass


class ModifierPanel:
    Add = ()

    AddToSelection = ()

    Delete = ()

    EnableShowEndResult = ()

    GetContexts = ()

    GetReplaceableObjRef = ()

    GetShowEndResult = ()

    IsValid = ()

    SetShowEndResult = ()

    thisown = ()

    def Add(self):
        pass

    def AddToSelection(self):
        pass

    def Delete(self):
        pass

    def EnableShowEndResult(self):
        pass

    def GetContexts(self):
        pass

    def GetReplaceableObjRef(self):
        pass

    def GetShowEndResult(self):
        pass

    def IsValid(self):
        pass

    def SetShowEndResult(self):
        pass


class Mtl(MtlBase):
    Ambient = ()
    CombineMaterials = ()
    Diffuse = ()
    SelfIllumColor = ()
    Shininess = ()
    ShinyStrength = ()
    Specular = ()
    SubMtls = ()
    thisown = ()

    def CombineMaterials(self, Mtr1, Mtl2, int):
        return Mtl()

    def CopySubMtl(self, HWND, ifrom, ito):
        pass

    def GetActiveTexmap(self):
        return MtlBase()

    def GetAmbient(self):
        return Color()

    def GetDiffuse(self):
        return Color()

    def GetNumSubMtls(self):
        return 0

    def GetSelfIllum(self):
        return 0.0

    def GetSelfIllumColor(self):
        return Color()

    def GetSelfIllumColorOn(self):
        return True

    def GetShininess(self):
        return 0.0

    def GetShinyStrength(self):
        return 0.0

    def GetSpecular(self):
        return Color()

    def GetSubMtl(self, int):
        return Mtl()

    def GetSubMtlSlotName(self, int):
        return WStr()

    def GetSubMtlTVName(self, int):
        return WStr()

    def GetXParency(self):
        return 0.0

    def SetActiveTexmap(self, MtlBase):
        pass

    def SetAmbient(self, Color, TimeValue):
        pass

    def SetDiffuse(self, Color, TimeValue):
        pass

    def SetShininess(self, float, TimeValue):
        pass

    def SetSpecular(self, Color, TimeValue):
        pass

    def SetSubMtl(self, int, Mtl):
        pass

    def SupportsRenderElements(self):
        return True

    def SupportsShaders(self):
        return True

    def VPDisplaySubMtl(self):
        return 0

    def WireSize(self):
        return 0.0


class MtlList:
    this = 0
    thisown = ()

    def Append(self, Mtl):
        pass

    def Delete(self):
        pass

    def GetCount(self):
        pass

    def GetItem(self, int):
        return Mtl()

    def Insert(self):
        pass

    def SetCount(self):
        pass

    def SetItem(self):
        pass


class MultiMtl(Mtl):
    thisown = ()

    def AddMtl(self):
        pass

    def GetSubMtlName(self):
        pass

    def RemoveMtl(self):
        pass

    def SetNumSubMtls(self):
        pass

    def SetSubMtlAndName(self):
        pass


class Names:
    AssignNew = ()

    GetSuffixLength = ()

    MakeNodeNameUnique = ()

    SetSuffixLength = ()

    thisown = ()

    def AssignNew(self):
        pass

    def GetSuffixLength(self):
        pass

    def MakeNodeNameUnique(self):
        pass

    def SetSuffixLength(self):
        pass


class NotificationCodes:
    AbNavigateUrl = 0
    ActionItemExecutionEnded = 0
    ActionItemExecutionStarted = 0
    ActionItemHotKeyPostExec = 0
    ActionItemHotKeyPreExec = 0
    ActionItemPostEndOverride = 0
    ActionItemPostStartOverride = 0
    ActionItemPreEndOverride = 0
    ActionItemPreStartOverride = 0
    ActiveViewportChanged = 0
    AnimateOff = 0
    AnimateOn = 0
    AnimLayersDisabled = 0
    AnimLayersEnabled = 0
    AppFrameThemeChanged = 0
    AtsPostRepathPhase = 0
    AtsPreRepathPhase = 0
    BeginRenderingActualFrame = 0
    BeginRenderingReflectRefractMap = 0
    BeginRenderingTonemappingImage = 0
    BitmapChanged = 0
    ByCategoryDisplayFilterChanged = 0
    ClassdescAdded = 0
    ClassdescLoaded = 0
    ClassdescReplaced = 0
    ColorChange = 0
    CustomAttributesAdded = 0
    CustomAttributesRemoved = 0
    CustomDisplayFilterChanged = 0
    D3dPostDeviceReset = 0
    D3dPreDeviceReset = 0
    ExportFailed = 0
    FailedDirectxMaterialTextureLoad = 0
    FileCheckStatus = 0
    FilelinkAttachFailed = 0
    FilelinkBindFailed = 0
    FilelinkDetachFailed = 0
    FilelinkPostAttach = 0
    FilelinkPostBind = 0
    FilelinkPostDetach = 0
    FilelinkPostReload = 0
    FilelinkPostReloadPrePrune = 0
    FilelinkPreAttach = 0
    FilelinkPreBind = 0
    FilelinkPreDetach = 0
    FilelinkPreReload = 0
    FilelinkReloadFailed = 0
    FileOpenFailed = 0
    FilePostMerge = 0
    FilePostOpen = 0
    FilePostOpenProcess = 0
    FilePostSave = 0
    FilePostSaveOld = 0
    FilePostSaveProcess = 0
    FilePreMerge = 0
    FilePreOpen = 0
    FilePreOpenProcess = 0
    FilePreSave = 0
    FilePreSaveOld = 0
    FilePreSaveProcess = 0
    FileStatusReadonly = 0
    HwTextureChanged = 0
    ImageViewerUpdate = 0
    ImportFailed = 0
    InternalUseStart = 0
    LayerCreated = 0
    LayerDeleted = 0
    LightingUnitDisplaySystemChange = 0
    ManipulateModeOff = 0
    ManipulateModeOn = 0
    MatlibPostMerge = 0
    MatlibPostOpen = 0
    MatlibPostSave = 0
    MatlibPreMerge = 0
    MatlibPreOpen = 0
    MatlibPreSave = 0
    ModpanelSelChanged = 0
    ModpanelSubobjectlevelChanged = 0
    MtlbaseParamdlgPostClose = 0
    MtlbaseParamdlgPreOpen = 0
    MtlRefadded = 0
    MtlRefdeleted = 0
    MxsPostStartup = 0
    MxsShutdown = 0
    MxsStartup = 0
    NamedSelSetCreated = 0
    NamedSelSetDeleted = 0
    NamedSelSetPostModify = 0
    NamedSelSetPreModify = 0
    NamedSelSetRenamed = 0
    NodeCloned = 0
    NodeCreated = 0
    NodeFreeze = 0
    NodeHide = 0
    NodeLayerChanged = 0
    NodeLinked = 0
    NodeNameSet = 0
    NodePostMtl = 0
    NodePreMtl = 0
    NodeRenamed = 0
    NodeUnfreeze = 0
    NodeUnhide = 0
    NodeUnlinked = 0
    ObjectDefinitionChangeBegin = 0
    ObjectDefinitionChangeEnd = 0
    ObjectXrefPostMerge = 0
    ObjectXrefPreMerge = 0
    OsThemeChanged = 0
    PluginLoaded = 0
    PostEditObjChange = 0
    PostExport = 0
    PostImageViewerDisplay = 0
    PostImport = 0
    PostMaxmainwindowShow = 0
    PostMergeProcess = 0
    PostMirrorNodes = 0
    PostModifierAdded = 0
    PostModifierDeleted = 0
    PostNodeBasicPropChanged = 0
    PostNodeBonePropChanged = 0
    PostNodeDisplayPropChanged = 0
    PostNodeGeneralPropChanged = 0
    PostNodeGiPropChanged = 0
    PostNodeMentalrayPropChanged = 0
    PostNodeRenderPropChanged = 0
    PostNodesCloned = 0
    PostNodeUserPropChanged = 0
    PostNotifydependents = 0
    PostProgress = 0
    PostRender = 0
    PostRendererChange = 0
    PostRenderframe = 0
    PostSceneReset = 0
    PreEditObjChange = 0
    PreExport = 0
    PreImageViewerDisplay = 0
    PreImport = 0
    PreMaxmainwindowShow = 0
    PreMirrorNodes = 0
    PreModifierAdded = 0
    PreModifierDeleted = 0
    PreNodeBasicPropChanged = 0
    PreNodeBonePropChanged = 0
    PreNodeDisplayPropChanged = 0
    PreNodeGeneralPropChanged = 0
    PreNodeGiPropChanged = 0
    PreNodeMentalrayPropChanged = 0
    PreNodeRenderPropChanged = 0
    PreNodesCloned = 0
    PreNodeUserPropChanged = 0
    PreNotifydependents = 0
    PreProgress = 0
    PreRender = 0
    PreRendererChange = 0
    PreRenderframe = 0
    ProxyTemporaryDisableEnd = 0
    ProxyTemporaryDisableStart = 0
    RadiosityPluginChanged = 0
    RadiosityprocessDone = 0
    RadiosityprocessReset = 0
    RadiosityprocessStarted = 0
    RadiosityprocessStopped = 0
    RenderPreeval = 0
    RenderPreevalFrameinfo = 0
    RendparamChanged = 0
    SceneAddedNode = 0
    ScenePostDeletedNode = 0
    ScenePostRefo = 0
    ScenePostUndo = 0
    ScenePreDeletedNode = 0
    ScenePreRedo = 0
    ScenePreUndo = 0
    SceneRedo = 0
    ScenestateDelete = 0
    ScenestatePostRestore = 0
    ScenestatePostSave = 0
    ScenestatePreRestore = 0
    ScenestatePreSave = 0
    ScenestateRename = 0
    SceneUndo = 0
    SceneXrefPostMerge = 0
    SceneXrefPreMerge = 0
    SelectionLock = 0
    SelectionsetChanged = 0
    SelectionUnlock = 0
    SelNodesPostDelete = 0
    SelNodesPreDelete = 0
    SpacemodeChange = 0
    SvDoubleclickGraphnode = 0
    SvPostLayoutChange = 0
    SvPreLayoutChange = 0
    SvSelectionsetChanged = 0
    SystemPostDirChange = 0
    SystemPostNew = 0
    SystemPostReset = 0
    SystemPreDirChange = 0
    SystemPreNew = 0
    SystemPreReset = 0
    SystemShutdown = 0
    SystemShutdown2 = 0
    SystemStartup = 0
    TabbedDialogCreated = 0
    TabbedDialogDeleted = 0
    thisown = ()
    TimerangeChange = 0
    TimeunitsChange = 0
    ToolbarsPostLoad = 0
    ToolbarsPreLoad = 0
    ToolpaletteMtlResume = 0
    ToolpaletteMtlSuspend = 0
    UnitsChange = 0
    ViewportChange = 0
    WmEnable = 0



class NotificationManager:
    Handlers = []

    def Register(self):
        pass

    def Unregister(self):
        pass


class ObjectList:
    this = 0
    thisown = ()

    def Append(self):
        pass

    def Delete(self):
        pass

    def GetCount(self):
        pass

    def GetItem(self):
        pass

    def Insert(self):
        pass

    def SetCount(self):
        pass

    def SetItem(self):
        pass


class ObjectState(Wrapper):
    this = ()

    def ApplyTM(self):
        pass

    def CopyMtl(self):
        pass

    def CopyTM(self):
        pass

    def DeleteObj(self):
        pass

    def Getobj(self):
        pass

    def GetTM(self):
        pass

    def Invalidate(self):
        pass

    def mtlValid(self):
        pass

    def OSClearFlag(self):
        pass

    def OSCopyFlag(self):
        pass

    def OSSetFlag(self):
        pass

    def OSTestFlag(self):
        pass

    def SetIdentityTM(self):
        pass

    def Setobj(self):
        pass

    def SetTM(self):
        pass

    def TMIsIdentity(self):
        pass

    def tmValid(self):
        pass

    def Validity(self):
        pass


class ParamDimensionBase(Wrapper):
    thisown = ()
    def Convert(self):
        pass

    def GetDimensionType(self):
        pass

    def UnConvert(self):
        pass


class ParamDimension(ParamDimensionBase):
    GetDefaultDim = ()

    GetStdAngleDim = ()

    GetStdColor255Dim = ()

    GetStdColorDim = ()

    GetStdNormalizedDim = ()

    GetStdPercentDim = ()

    GetStdSegmentsDim = ()

    GetStdTimeDim = ()

    GetStdWorldDim = ()

    def GetDefaultDim(self):
        pass

    def GetDimensionName(self):
        pass

    def GetDimScale(self):
        pass

    def GetStdAngleDim(self):
        pass

    def GetStdColor255Dim(self):
        pass

    def GetStdColorDim(self):
        pass

    def GetStdNormalizedDim(self):
        pass

    def GetStdPercentDim(self):
        pass

    def GetStdSegmentsDim(self):
        pass

    def GetStdTimeDim(self):
        pass

    def GetStdWorldDim(self):
        pass

    def SetDimScale(self):
        pass


class Parameter:
    Controller = ()

    IsAnimatable = ()

    IsArrayData = ()

    IsArrayParameter = ()

    IsObsolete = ()

    IsReadOnly = ()

    Name = ()

    TabIndex = ()

    thisown = ()

    Type = ()

    Value = ()

    def GetController(self):
        pass

    def GetName(self):
        pass

    def GetTabIndex(self):
        pass

    def GetType(self):
        pass

    def GetValue(self):
        pass

    def IsAnimatable(self):
        pass

    def IsArrayData(self):
        pass

    def IsArrayParameter(self):
        pass

    def IsObsolete(self):
        pass

    def IsReadOnly(self):
        pass

    def ReplaceController(self):
        pass

    def SetController(self):
        pass

    def SetValue(self):
        pass


class ParameterBlock:
    NumParameters = ()
    Parameters = ()
    thisown = ()
    class Radius:
        Value = 0
    class Width:
        Value = 0
    class Height:
        Value = 0
    class Length:
        Value = 0
    class BendAngle:
        Value = 0
    class radius1:
        Value = 0
    class radius2:
        Value = 0
    class size:
        Value = 0
    class text:
        Value = ''

    def Count(self):
        pass

    def GetItem(self):
        pass

    def GetParamByName(self):
        pass



class PathManager:
    GetAnimationDir = ()
    GetAppExchangeStorePrivateDir = ()
    GetAppExchangeStorePublicDir = ()
    GetArchivesDir = ()
    GetAutobackDir = ()
    GetAutodeskCloudDir = ()
    GetDownloadDir = ()
    GetDriversDir = ()
    GetExportDir = ()
    GetExpressionDir = ()
    GetFontDir = ()
    GetHelpDir = ()
    GetImageDir = ()
    GetImportDir = ()
    GetManagedAssembliesDir = ()
    GetMarketDefaultsDir = ()
    GetMatlibDir = ()
    GetMaxdataDir = ()
    GetMaxstartDir = ()
    GetMaxSysRootDir = ()
    GetNonLocalizedPluginCfg = ()
    GetNonLocalizedUIDataDir = ()
    GetPageFileDir = ()
    GetPhotometricDir = ()
    GetPlugcfgDir = ()
    GetPreviewDir = ()
    GetProjectFolderDir = ()
    GetProxiesDir = ()
    GetRenderAssetsDir = ()
    GetRenderOutputDir = ()
    GetRenderPresetsDir = ()
    GetSceneDir = ()
    GetScriptsDir = ()
    GetShaderCacheDir = ()
    GetSoundDir = ()
    GetStartupscriptsDir = ()
    GetTempDir = ()
    GetUiDir = ()
    GetUserIconsDir = ()
    GetUserMacrosDir = ()
    GetUserScriptsDir = ()
    GetUserStartupscriptsDir = ()
    GetVpostDir = ()
    SetAnimationDir = ()
    SetArchivesDir = ()
    SetAutobackDir = ()
    SetAutodeskCloudDir = ()
    SetDownloadDir = ()
    SetDriversDir = ()
    SetExportDir = ()
    SetExpressionDir = ()
    SetFontDir = ()
    SetHelpDir = ()
    SetImageDir = ()
    SetImportDir = ()
    SetManagedAssembliesDir = ()
    SetMarketDefaultsDir = ()
    SetMatlibDir = ()
    SetMaxdataDir = ()
    SetMaxstartDir = ()
    SetMaxSysRootDir = ()
    SetNonLocalizedPluginCfg = ()
    SetNonLocalizedUIDataDir = ()
    SetPageFileDir = ()
    SetPhotometricDir = ()
    SetPlugcfgDir = ()
    SetPreviewDir = ()
    SetProjectFolderDir = ()
    SetProxiesDir = ()
    SetRenderAssetsDir = ()
    SetRenderOutputDir = ()
    SetRenderPresetsDir = ()
    SetSceneDir = ()
    SetScriptsDir = ()
    SetShaderCacheDir = ()
    SetSoundDir = ()
    SetStartupscriptsDir = ()
    SetTempDir = ()
    SetUiDir = ()
    SetUserIconsDir = ()
    SetUserMacrosDir = ()
    SetUserScriptsDir = ()
    SetUserStartupscriptsDir = ()
    SetVpostDir = ()
    thisown = ()

    def GetAnimationDir(self):
        return ''

    def GetAppExchangeStorePrivateDir(self):
        return ''

    def GetAppExchangeStorePublicDir(self):
        return ''

    def GetArchivesDir(self):
        return ''

    def GetAutobackDir(self):
        return ''

    def GetAutodeskCloudDir(self):
        return ''

    def GetDownloadDir(self):
        return ''

    def GetDriversDir(self):
        return ''

    def GetExportDir(self):
        return ''

    def GetExpressionDir(self):
        return ''

    def GetFontDir(self):
        return ''

    def GetHelpDir(self):
        return ''

    def GetImageDir(self):
        return ''

    def GetImportDir(self):
        return ''

    def GetManagedAssembliesDir(self):
        return ''

    def GetMarketDefaultsDir(self):
        return ''

    def GetMatlibDir(self):
        return ''

    def GetMaxdataDir(self):
        return ''

    def GetMaxstartDir(self):
        return ''

    def GetMaxSysRootDir(self):
        return ''

    def GetNonLocalizedPluginCfg(self):
        return ''

    def GetNonLocalizedUIDataDir(self):
        return ''

    def GetPageFileDir(self):
        return ''

    def GetPhotometricDir(self):
        return ''

    def GetPlugcfgDir(self):
        return ''

    def GetPreviewDir(self):
        return ''

    def GetProjectFolderDir(self):
        return ''

    def GetProxiesDir(self):
        return ''

    def GetRenderAssetsDir(self):
        return ''

    def GetRenderOutputDir(self):
        return ''

    def GetRenderPresetsDir(self):
        return ''

    def GetSceneDir(self):
        return ''

    def GetScriptsDir(self):
        return ''

    def GetShaderCacheDir(self):
        return ''

    def GetSoundDir(self):
        return ''

    def GetStartupscriptsDir(self):
        return ''

    def GetTempDir(self):
        return ''

    def GetUiDir(self):
        return ''

    def GetUserIconsDir(self):
        return ''

    def GetUserMacrosDir(self):
        return ''

    def GetUserScriptsDir(self):
        return ''

    def GetUserStartupscriptsDir(self):
        return ''

    def GetVpostDir(self):
        return ''

    def SetAnimationDir(self, dir):
        pass

    def SetArchivesDir(self, dir):
        pass

    def SetAutobackDir(self, dir):
        pass

    def SetAutodeskCloudDir(self, dir):
        pass

    def SetDownloadDir(self, dir):
        pass

    def SetDriversDir(self, dir):
        pass

    def SetExportDir(self, dir):
        pass

    def SetExpressionDir(self, dir):
        pass

    def SetFontDir(self, dir):
        pass

    def SetHelpDir(self, dir):
        pass

    def SetImageDir(self, dir):
        pass

    def SetImportDir(self, dir):
        pass

    def SetManagedAssembliesDir(self, dir):
        pass

    def SetMarketDefaultsDir(self, dir):
        pass

    def SetMatlibDir(self, dir):
        pass

    def SetMaxdataDir(self, dir):
        pass

    def SetMaxstartDir(self, dir):
        pass

    def SetMaxSysRootDir(self, dir):
        pass

    def SetNonLocalizedPluginCfg(self, dir):
        pass

    def SetNonLocalizedUIDataDir(self, dir):
        pass

    def SetPageFileDir(self, dir):
        pass

    def SetPhotometricDir(self, dir):
        pass

    def SetPlugcfgDir(self, dir):
        pass

    def SetPreviewDir(self, dir):
        pass

    def SetProjectFolderDir(self, dir):
        pass

    def SetProxiesDir(self, dir):
        pass

    def SetRenderAssetsDir(self, dir):
        pass

    def SetRenderOutputDir(self, dir):
        pass

    def SetRenderPresetsDir(self, dir):
        pass

    def SetSceneDir(self, dir):
        pass

    def SetScriptsDir(self, dir):
        pass

    def SetShaderCacheDir(self, dir):
        pass

    def SetSoundDir(self, dir):
        pass

    def SetStartupscriptsDir(self, dir):
        pass

    def SetTempDir(self, dir):
        pass

    def SetUiDir(self, dir):
        pass

    def SetUserIconsDir(self, dir):
        pass

    def SetUserMacrosDir(self, dir):
        pass

    def SetUserScriptsDir(self, dir):
        pass

    def SetUserStartupscriptsDir(self, dir):
        pass

    def SetVpostDir(self, dir):
        pass


class PBBitmap(Wrapper):
    this = 0
    thisown = ()

    def Clone(self):
        pass

    def GetBitmap(self):
        pass

    def GetBitmapInfo(self):
        pass

    def Load(self):
        pass


class PCharList:
    this = 0
    thisown = ()

    def Append(self):
        pass

    def Delete(self):
        pass

    def GetCount(self):
        pass

    def GetItem(self):
        pass

    def Insert(self):
        pass

    def SetCount(self):
        pass

    def SetItem(self):
        pass


class PivotMode:
    Hierarchy = 0
    NoPivot = 0
    Object = 0
    Pivot = 0
    thisown = ()


class PluginDll:
    Classes = ()

    Description = ()

    FilePath = ()

    Loaded = ()

    NumClasses = ()

    thisown = ()

    def GetClass(self):
        pass

    def GetDescription(self):
        pass

    def GetFilePath(self):
        pass

    def GetNumClasses(self):
        pass

    def IsLoaded(self):
        pass



class PluginManager:
    Classes = ()
    GetClassInfo = ()
    GetClassList = ()
    GetNumClasses = ()
    GetNumPluginDlls = ()
    GetPluginDll = ()
    PluginDlls = ()
    thisown = ()

    def GetClassInfo(self, int):
        return ClassInfo()

    def GetClassList(self):
        return ClassList()

    def GetNumClasses(self):
        return 0

    def GetNumPluginDlls(self):
        return 0

    def GetPluginDll(self):
        return PluginDll()


class Point2(Wrapper):
    GetOrigin = ()
    GetXAxis = ()
    GetYAxis = ()
    thisown = ()
    X = ()
    Y = ()

    def DotProd(self, Point2):
        return 0.0

    def Equals(self, Point2):
        return True

    def GetLength(self):
        return 0.0

    def GetMaxComponent(self):
        return 0

    def GetMinComponent(self):
        return 0

    def GetOrigin(self):
        return Point2()

    def GetX(self):
        return 0.0

    def GetXAxis(self):
        return Point2()

    def GetY(self):
        return 0.0

    def GetYAxis(self):
        return Point2()

    def LengthUnify(self):
        return 0.0

    def Normalize(self):
        return Point2()

    def Set(self, x, y):
        return Point2()

    def SetX(self, float):
        pass

    def SetY(self, float):
        pass

    def Unify(self):
        return Point2()


class Point2List:
    this = 0
    thisown = ()

    def Append(self, Point2):
        pass

    def Delete(self, int):
        pass

    def GetCount(self):
        return 0

    def GetItem(self, int):
        return Point2()

    def Insert(self, Point2, int):
        pass

    def SetCount(self, int):
        pass

    def SetItem(self, int, Point2):
        pass


class Point3(Wrapper):
    GetOrigin = ()
    GetXAxis = ()
    GetYAxis = ()
    GetZAxis = ()
    thisown = ()
    X = ()
    Y = ()
    Z = ()

    def __init__(self, x, y, z):
        pass

    def Equals(self, Point3, epsilon):
        return True

    def FNormalize(self):
        return Point3()

    def GetFLength(self):
        return 0.0

    def GetLength(self):
        return 0.0

    def GetLengthSquared(self):
        return 0.0

    def GetMaxComponent(self):
        return 0

    def GetMinComponent(self):
        return 0

    def GetOrigin(self):
        return Point3()

    def GetX(self):
        return 0.0

    def GetXAxis(self):
        return Point3()

    def GetY(self):
        return 0.0

    def GetYAxis(self):
        return Point3()

    def GetZ(self):
        return 0.0

    def GetZAxis(self):
        return Point3()

    def LengthUnify(self):
        return 0.0

    def Normalize(self):
        return Point3()

    def Set(self, x, y, z):
        return Point3()

    def SetX(self, float):
        pass

    def SetY(self, float):
        pass

    def SetZ(self, float):
        pass

    def Unify(self):
        return Point3()


class Point3List:
    this = 0
    thisown = ()

    def Append(self, Point3):
        pass

    def Delete(self, int):
        pass

    def GetCount(self):
        return 0

    def GetItem(self, int):
        return Point3()

    def Insert(self, Point3, int):
        pass

    def SetCount(self, int):
        pass

    def SetItem(self, int, Point3):
        pass


class Point4(Wrapper):
    GetOrigin = ()
    GetWAxis = ()
    GetXAxis = ()
    GetYAxis = ()
    GetZAxis = ()
    thisown = ()
    W = ()
    X = ()
    Y = ()
    Z = ()

    def Equals(self, Point4):
        pass

    def FNormalize(self):
        pass

    def GetFLength(self):
        pass

    def GetLength(self):
        pass

    def GetLengthSquared(self):
        pass

    def GetMaxComponent(self):
        pass

    def GetMinComponent(self):
        pass

    def GetOrigin(self):
        pass

    def GetW(self):
        pass

    def GetWAxis(self):
        pass

    def GetX(self):
        pass

    def GetXAxis(self):
        pass

    def GetY(self):
        pass

    def GetYAxis(self):
        pass

    def GetZ(self):
        pass

    def GetZAxis(self):
        pass

    def LengthUnify(self):
        pass

    def Normalize(self):
        pass

    def Set(self):
        pass

    def SetW(self):
        pass

    def SetX(self):
        pass

    def SetY(self):
        pass

    def SetZ(self):
        pass

    def Unify(self):
        pass


class Point4List:
    this = 0
    thisown = ()

    def Append(self, Point4):
        pass

    def Delete(self, int):
        pass

    def GetCount(self):
        pass

    def GetItem(self, int):
        return Point4()

    def Insert(self):
        pass

    def SetCount(self):
        pass

    def SetItem(self):
        pass


class PolyLine(Wrapper):
    thisown = ()

    def Append(self):
        pass

    def BuildBoundingBox(self):
        pass

    def Close(self):
        pass

    def CopyFrom(self):
        pass

    def CurveLength(self):
        pass

    def Delete(self):
        pass

    def GetBoundingBox(self):
        pass

    def GetFlags(self):
        pass

    def GetMatID(self):
        pass

    def GetNumPoints(self):
        pass

    def GetSmoothingMap(self):
        pass

    def HitsPolyLine(self):
        pass

    def HitsSegment(self):
        pass

    def Init(self):
        pass

    def Insert(self):
        pass

    def InterpCurve3D(self):
        pass

    def InterpPiece3D(self):
        pass

    def IsClockWise(self):
        pass

    def IsClosed(self):
        pass

    def IsNoSelfInt(self):
        pass

    def IsOpen(self):
        pass

    def Open(self):
        pass

    def Reverse(self):
        pass

    def Segments(self):
        pass

    def SelfIntersects(self):
        pass

    def SetNoSelfInt(self):
        pass

    def SetNumPoints(self):
        pass

    def SpliceLine(self):
        pass

    def SurroundsPoint(self):
        pass

    def Swap(self):
        pass

    def TangentCurve3D(self):
        pass

    def TangentPiece3D(self):
        pass

    def Transform(self):
        pass


class PolyPt(Wrapper):
    this = 0
    thisown = ()

    def GetAux(self):
        pass

    def GetFlags(self):
        pass

    def GetFlags2(self):
        pass

    def GetMatID(self):
        pass

    def GetPoint(self):
        pass

    def SetAux(self):
        pass

    def SetFlags(self):
        pass

    def SetFlags2(self):
        pass

    def SetMatID(self):
        pass

    def SetPoint(self):
        pass


class PolyShape(Wrapper):
    thisown = ()

    def Append(self):
        pass

    def BuildBoundingBox(self):
        pass

    def CopyFrom(self):
        pass

    def DeepCopy(self):
        pass

    def Delete(self):
        pass

    def FreeChannels(self):
        pass

    def GetBoundingBox(self):
        pass

    def GetDeformBBox(self):
        pass

    def GetDisplayFlags(self):
        pass

    def GetFlags(self):
        pass

    def GetLine(self):
        pass

    def GetMatID(self):
        pass

    def GetNumLines(self):
        pass

    def Init(self):
        pass

    def Insert(self):
        pass

    def InvalidateCapCache(self):
        pass

    def InvalidateGeomCache(self):
        pass

    def NewAndCopyChannels(self):
        pass

    def NewLine(self):
        pass

    def NewShape(self):
        pass

    def Reverse(self):
        pass

    def SetNumLines(self):
        pass

    def ShallowCopy(self):
        pass

    def Transform(self):
        pass

    def UpdateCachedHierarchy(self):
        pass

    def UpdateSels(self):
        pass

    def VertexTempSel(self):
        pass


class PreferencesFileEncoding:
    CodePageForLanguage = ()

    DefaultTextLoadCodePage = ()

    DefaultTextSaveCodePage = ()

    LanguageToUseForFileIO = ()

    LegacyFilesCanBeStoredUsingUTF8 = ()

    OverrideLanguageSpecifiedInSceneFile = ()

    SetLanguageToUseForFileIO = ()

    SetLegacyFilesCanBeStoredUsingUTF8 = ()

    SetOverrideLanguageSpecifiedInSceneFile = ()

    SetUseCodePageSpecifiedInSceneFile = ()

    thisown = ()

    UseCodePageSpecifiedInSceneFile = ()

    def CodePageForLanguage(self):
        pass

    def DefaultTextLoadCodePage(self):
        pass

    def DefaultTextSaveCodePage(self):
        pass

    def LanguageToUseForFileIO(self):
        pass

    def LegacyFilesCanBeStoredUsingUTF8(self):
        pass

    def OverrideLanguageSpecifiedInSceneFile(self):
        pass

    def SetLanguageToUseForFileIO(self):
        pass

    def SetLegacyFilesCanBeStoredUsingUTF8(self):
        pass

    def SetOverrideLanguageSpecifiedInSceneFile(self):
        pass

    def SetUseCodePageSpecifiedInSceneFile(self):
        pass

    def UseCodePageSpecifiedInSceneFile(self):
        pass


class PreferencesRendering:
    GetRendDither256 = ()

    GetRendDitherTrue = ()

    GetRendFieldOrder = ()

    GetRendMultiThread = ()

    GetRendNThSerial = ()

    GetRendNTSC_PAL = ()

    GetRendSuperBlackThresh = ()

    GetRendVidCorrectMethod = ()

    SetRendDither256 = ()

    SetRendDitherTrue = ()

    SetRendFieldOrder = ()

    SetRendMultiThread = ()

    SetRendNThSerial = ()

    SetRendNTSC_PAL = ()

    SetRendSuperBlackThresh = ()

    SetRendVidCorrectMethod = ()

    thisown = ()

    def GetRendDither256(self):
        pass

    def GetRendDitherTrue(self):
        pass

    def GetRendFieldOrder(self):
        pass

    def GetRendMultiThread(self):
        pass

    def GetRendNThSerial(self):
        pass

    def GetRendNTSC_PAL(self):
        pass

    def GetRendSuperBlackThresh(self):
        pass

    def GetRendVidCorrectMethod(self):
        pass

    def SetRendDither256(self):
        pass

    def SetRendDitherTrue(self):
        pass

    def SetRendFieldOrder(self):
        pass

    def SetRendMultiThread(self):
        pass

    def SetRendNThSerial(self):
        pass

    def SetRendNTSC_PAL(self):
        pass

    def SetRendSuperBlackThresh(self):
        pass

    def SetRendVidCorrectMethod(self):
        pass


class PreviewParams(Wrapper):
    GetViewportPreview = ()

    thisown = ()

    def GetDspBkg(self):
        pass

    def GetDspCameras(self):
        pass

    def GetDspFrameNums(self):
        pass

    def GetDspGeometry(self):
        pass

    def GetDspGrid(self):
        pass

    def GetDspHelpers(self):
        pass

    def GetDspLights(self):
        pass

    def GetDspSafeFrame(self):
        pass

    def GetDspShapes(self):
        pass

    def GetDspSpaceWarps(self):
        pass

    def GetEnd(self):
        pass

    def GetFps(self):
        pass

    def GetOutputType(self):
        pass

    def GetPctSize(self):
        pass

    def GetRndLevel(self):
        pass

    def GetSkip(self):
        pass

    def GetStart(self):
        pass

    def GetViewportPreview(self):
        pass

    def SetDspBkg(self):
        pass

    def SetDspCameras(self):
        pass

    def SetDspFrameNums(self):
        pass

    def SetDspGeometry(self):
        pass

    def SetDspGrid(self):
        pass

    def SetDspHelpers(self):
        pass

    def SetDspLights(self):
        pass

    def SetDspSafeFrame(self):
        pass

    def SetDspShapes(self):
        pass

    def SetDspSpaceWarps(self):
        pass

    def SetEnd(self):
        pass

    def SetFps(self):
        pass

    def SetOutputType(self):
        pass

    def SetPctSize(self):
        pass

    def SetRndLevel(self):
        pass

    def SetSkip(self):
        pass

    def SetStart(self):
        pass


class QuadMenu(FPInterface):
    Menus = ()

    NumMenus = ()

    thisown = ()

    def GetMenu(self):
        pass

    def GetNumMenus(self):
        pass


class Quat(Wrapper):
    thisown = ()
    W = ()
    X = ()
    Y = ()
    Z = ()

    def Conjugate(self):
        return Quat()

    def Equals(self, Quat, epsilon):
        return True

    def Exp(self):
        return Quat()

    def GetEuler(self, x, y, z):
        pass

    def GetW(self):
        return 0.0

    def GetX(self):
        return 0.0

    def GetY(self):
        return 0.0

    def GetZ(self):
        return 0.0

    def Identity(self):
        pass

    def Inverse(self):
        return Quat()

    def Invert(self):
        return Quat()

    def IsIdentity(self):
        return 0

    def LogN(self):
        return Quat()

    def MakeClosest(self, Quat):
        return Quat()

    def Minus(self, Quat):
        return Quat()

    def Normalize(self):
        return Quat()

    def Plus(self, Quat):
        return Quat()

    def Scalar(self):
        return 0.0

    def Set(self, values):
        return Quat()

    def SetEuler(self, x, y, z):
        return Quat()

    def SetW(self, float):
        pass

    def SetX(self, float):
        pass

    def SetY(self, float):
        pass

    def SetZ(self, float):
        pass

    def Vector(self):
        return Point3()


class QuatList:
    this = 0
    thisown = ()

    def Append(self):
        pass

    def Delete(self):
        pass

    def GetCount(self):
        pass

    def GetItem(self):
        pass

    def Insert(self):
        pass

    def SetCount(self):
        pass

    def SetItem(self):
        pass


class RadiosityEffect(SpecialFX):
    thisown = ()

    def SetActive(self):
        pass

    def UseLight(self):
        pass


class Ray(Wrapper):
    Direction = ()

    Point = ()

    thisown = ()

    def GetDirection(self):
        pass

    def GetPoint(self):
        pass

    def SetDirection(self):
        pass

    def SetPoint(self):
        pass


class RayList:
    this = 0
    thisown = ()

    def Append(self):
        pass

    def Delete(self):
        pass

    def GetCount(self):
        pass

    def GetItem(self):
        pass

    def Insert(self):
        pass

    def SetCount(self):
        pass

    def SetItem(self):
        pass


class RealWorldMapSizeInterface(FPInterface):
    thisown = ()

    def GetUsePhysicalScaleUVs(self):
        pass

    def SetUsePhysicalScaleUVs(self):
        pass


class ReferenceMessagePartIds:
    PartAll = 0
    PartDispPropAllEdges = 0
    PartDispPropBackcull = 0
    PartDispPropBoneAsLine = 0
    PartDispPropBoneOnly = 0
    PartDispPropBoxMode = 0
    PartDispPropColorVerts = 0
    PartDispPropIgnoreExtents = 0
    PartDispPropIsFrozen = 0
    PartDispPropIsHidden = 0
    PartDispPropShowFrznWithMtl = 0
    PartDispPropShowPath = 0
    PartDispPropVertTicks = 0
    PartDispPropXrayMtl = 0
    PartExcludeRadiosity = 0
    PartGiContrastThreshold = 0
    PartGiDiffuse = 0
    PartGiExcluded = 0
    PartGiExcludefromregathering = 0
    PartGiInitialMeshSize = 0
    PartGiMeshingenabled = 0
    PartGiMeshsize = 0
    PartGiMinMeshSize = 0
    PartGiNbrefinesteps = 0
    PartGiOccluder = 0
    PartGiRaymult = 0
    PartGiReceiver = 0
    PartGiSpecular = 0
    PartGiStoreillummesh = 0
    PartGiUseAdaptiveSubdivision = 0
    PartGiUseglobalmeshing = 0
    PartHidestate = 0
    PartMxsPropchange = 0
    PartObj = 0
    PartObjectType = 0
    PartRendPropCastShadow = 0
    PartRendPropInheritVis = 0
    PartRendPropPrimaryInvisibility = 0
    PartRendPropRcvShadow = 0
    PartRendPropRenderable = 0
    PartRendPropRenderOccluded = 0
    PartRendPropSecondaryInvisibility = 0
    PartRendPropVisibility = 0
    PartTm = 0


class ReferenceTargetList:
    this = 0
    thisown = ()

    def Append(self):
        pass

    def Delete(self):
        pass

    def GetCount(self):
        pass

    def GetItem(self):
        pass

    def Insert(self):
        pass

    def SetCount(self):
        pass

    def SetItem(self):
        pass


class RenderElement(SpecialFX):
    ElementName = ()

    Enabled = ()

    FilterEnabled = ()

    PBBitmap = ()

    thisown = ()

    def AtmosphereApplied(self):
        pass

    def BlendOnMultipass(self):
        pass

    def GetElementName(self):
        pass

    def GetPBBitmap(self):
        pass

    def IsEnabled(self):
        pass

    def IsFilterEnabled(self):
        pass

    def SetElementName(self):
        pass

    def SetEnabled(self):
        pass

    def SetFilterEnabled(self):
        pass

    def SetPBBitmap(self):
        pass

    def ShadowsApplied(self):
        pass


class RenderElementMgr(FPInterface):
    CombustionOutput = ()

    CombustionOutputEnabled = ()

    DisplayElements = ()

    ElementsActive = ()

    RenderElements = ()

    thisown = ()

    def AddRenderElement(self):
        pass

    def GetCombustionOutput(self):
        pass

    def GetCombustionOutputEnabled(self):
        pass

    def GetDisplayElements(self):
        pass

    def GetElementsActive(self):
        pass

    def GetRenderElement(self):
        pass

    def NumRenderElements(self):
        pass

    def RemoveAllRenderElements(self):
        pass

    def RemoveRenderElement(self):
        pass

    def SetCombustionOutput(self):
        pass

    def SetCombustionOutputEnabled(self):
        pass

    def SetDisplayElements(self):
        pass

    def SetElementsActive(self):
        pass


class RenderExecute:
    Close = ()

    CloseCurrent = ()

    CreatePreview = ()

    Open = ()

    QuickRender = ()

    RenderFrame = ()

    thisown = ()

    def Close(self):
        pass

    def CloseCurrent(self):
        pass

    def CreatePreview(self):
        pass

    def Open(self):
        pass

    def QuickRender(self):
        pass

    def RenderFrame(self):
        pass


class RenderSettingID:
    ActiveShade = 0
    MaterialEditor = 0
    Production = 0
    thisown = ()


#qff
class RenderSettings:
    BeginProgressiveMode = ()
    CancelDialog = ()
    CloseDialog = ()
    ColorById = ()
    CommitDialogParameters = ()
    CreateDefault = ()
    CreateDefaultScanline = ()
    DialogOpen = ()
    EndProgressiveMode = ()
    FormatRenderTime = ()
    Get = ()
    GetActualMEditRenderer = ()
    GetApertureWidth = ()
    GetAreaType = ()
    GetAtmosphere = ()
    GetCamera = ()
    GetColorCheck = ()
    GetCurrent = ()
    GetCurrentRenderElementManager = ()
    GetCurrentSetting = ()
    GetDefaultRendererClassID = ()
    GetDeviceBitmapInfo = ()
    GetDisplacement = ()
    GetDraft = ()
    GetEffects = ()
    GetEnd = ()
    GetFileBitmapInfo = ()
    GetFileNumberBase = ()
    GetForce2Side = ()
    GetFrameList = ()
    GetHeight = ()
    GetHidden = ()
    GetImageAspectRatio = ()
    GetImageSequenceType = ()
    GetLastRenderedImage = ()
    GetLocalPreScript = ()
    GetMEditRenderer = ()
    GetMEditRendererLocked = ()
    GetMEditRendererLocked_Default = ()
    GetNThFrame = ()
    GetOutputFile = ()
    GetPickFramesString = ()
    GetPixelAspectRatio = ()
    GetPostScriptFile = ()
    GetPreScriptFile = ()
    GetPresetCount = ()
    GetPresetDisplayName = ()
    GetPresetFileName = ()
    GetProduction = ()
    GetRenderElementMgr = ()
    GetSaveFile = ()
    GetShowVFB = ()
    GetSimplifyAreaLights = ()
    GetSkipFrames = ()
    GetStart = ()
    GetSuperBlack = ()
    GetTimeType = ()
    GetToFields = ()
    GetUseActiveView = ()
    GetUseDevice = ()
    GetUseDraft = ()
    GetUseImageSequence = ()
    GetUseIterative = ()
    GetUseNet = ()
    GetUsePostScript = ()
    GetUsePreScript = ()
    GetViewID = ()
    GetViewParamsFromNode = ()
    GetWidth = ()
    InProgressiveMode = ()
    IsActive = ()
    OpenDialog = ()
    Set = ()
    SetApertureWidth = ()
    SetAreaType = ()
    SetAtmosphere = ()
    SetCamera = ()
    SetColorCheck = ()
    SetCurrent = ()
    SetCurrentSetting = ()
    SetDefaultRendererClassID = ()
    SetDisplacement = ()
    SetDraft = ()
    SetEffects = ()
    SetEnd = ()
    SetFileNumberBase = ()
    SetForce2Side = ()
    SetHeight = ()
    SetHidden = ()
    SetImageSequenceType = ()
    SetLocalPreScript = ()
    SetMEditRenderer = ()
    SetMEditRendererLocked = ()
    SetMEditRendererLocked_Default = ()
    SetNThFrame = ()
    SetOutputFile = ()
    SetPixelAspectRatio = ()
    SetPostScriptFile = ()
    SetPreScriptFile = ()
    SetProduction = ()
    SetSaveFile = ()
    SetShowVFB = ()
    SetSimplifyAreaLights = ()
    SetSkipFrames = ()
    SetStart = ()
    SetSuperBlack = ()
    SetTimeType = ()
    SetToFields = ()
    SetupParameters = ()
    SetUseActiveView = ()
    SetUseDevice = ()
    SetUseDraft = ()
    SetUseImageSequence = ()
    SetUseIterative = ()
    SetUseNet = ()
    SetUsePostScript = ()
    SetUsePreScript = ()
    SetViewID = ()
    SetWidth = ()
    ShouldContinueOnError = ()
    thisown = ()
    UpdateDialogParameters = ()

    def BeginProgressiveMode(self):
        pass

    def CancelDialog(self):
        pass

    def CloseDialog(self):
        pass

    def ColorById(self):
        pass

    def CommitDialogParameters(self):
        pass

    def CreateDefault(self):
        pass

    def CreateDefaultScanline(self):
        pass

    def DialogOpen(self):
        pass

    def EndProgressiveMode(self):
        pass

    def FormatRenderTime(self):
        pass

    def Get(self):
        pass

    def GetActualMEditRenderer(self):
        pass

    def GetApertureWidth(self):
        pass

    def GetAreaType(self):
        pass

    def GetAtmosphere(self):
        pass

    def GetCamera(self):
        pass

    def GetColorCheck(self):
        pass

    def GetCurrent(self):
        pass

    def GetCurrentRenderElementManager(self):
        pass

    def GetCurrentSetting(self):
        pass

    def GetDefaultRendererClassID(self):
        pass

    def GetDeviceBitmapInfo(self):
        pass

    def GetDisplacement(self):
        pass

    def GetDraft(self):
        pass

    def GetEffects(self):
        pass

    def GetEnd(self):
        pass

    def GetFileBitmapInfo(self):
        pass

    def GetFileNumberBase(self):
        pass

    def GetForce2Side(self):
        pass

    def GetFrameList(self):
        pass

    def GetHeight(self):
        pass

    def GetHidden(self):
        pass

    def GetImageAspectRatio(self):
        pass

    def GetImageSequenceType(self):
        pass

    def GetLastRenderedImage(self):
        pass

    def GetLocalPreScript(self):
        pass

    def GetMEditRenderer(self):
        pass

    def GetMEditRendererLocked(self):
        pass

    def GetMEditRendererLocked_Default(self):
        pass

    def GetNThFrame(self):
        pass

    def GetOutputFile(self):
        pass

    def GetPickFramesString(self):
        pass

    def GetPixelAspectRatio(self):
        pass

    def GetPostScriptFile(self):
        pass

    def GetPreScriptFile(self):
        pass

    def GetPresetCount(self):
        pass

    def GetPresetDisplayName(self):
        pass

    def GetPresetFileName(self):
        pass

    def GetProduction(self):
        pass

    def GetRenderElementMgr(self):
        pass

    def GetSaveFile(self):
        pass

    def GetShowVFB(self):
        pass

    def GetSimplifyAreaLights(self):
        pass

    def GetSkipFrames(self):
        pass

    def GetStart(self):
        pass

    def GetSuperBlack(self):
        pass

    def GetTimeType(self):
        pass

    def GetToFields(self):
        pass

    def GetUseActiveView(self):
        pass

    def GetUseDevice(self):
        pass

    def GetUseDraft(self):
        pass

    def GetUseImageSequence(self):
        pass

    def GetUseIterative(self):
        pass

    def GetUseNet(self):
        pass

    def GetUsePostScript(self):
        pass

    def GetUsePreScript(self):
        pass

    def GetViewID(self):
        pass

    def GetViewParamsFromNode(self):
        pass

    def GetWidth(self):
        pass

    def InProgressiveMode(self):
        pass

    def IsActive(self):
        pass

    def OpenDialog(self):
        pass

    def Set(self):
        pass

    def SetApertureWidth(self):
        pass

    def SetAreaType(self):
        pass

    def SetAtmosphere(self):
        pass

    def SetCamera(self):
        pass

    def SetColorCheck(self):
        pass

    def SetCurrent(self):
        pass

    def SetCurrentSetting(self):
        pass

    def SetDefaultRendererClassID(self):
        pass

    def SetDisplacement(self):
        pass

    def SetDraft(self):
        pass

    def SetEffects(self):
        pass

    def SetEnd(self):
        pass

    def SetFileNumberBase(self):
        pass

    def SetForce2Side(self):
        pass

    def SetHeight(self):
        pass

    def SetHidden(self):
        pass

    def SetImageSequenceType(self):
        pass

    def SetLocalPreScript(self):
        pass

    def SetMEditRenderer(self):
        pass

    def SetMEditRendererLocked(self):
        pass

    def SetMEditRendererLocked_Default(self):
        pass

    def SetNThFrame(self):
        pass

    def SetOutputFile(self):
        pass

    def SetPixelAspectRatio(self):
        pass

    def SetPostScriptFile(self):
        pass

    def SetPreScriptFile(self):
        pass

    def SetProduction(self):
        pass

    def SetSaveFile(self):
        pass

    def SetShowVFB(self):
        pass

    def SetSimplifyAreaLights(self):
        pass

    def SetSkipFrames(self):
        pass

    def SetStart(self):
        pass

    def SetSuperBlack(self):
        pass

    def SetTimeType(self):
        pass

    def SetToFields(self):
        pass

    def SetupParameters(self):
        pass

    def SetUseActiveView(self):
        pass

    def SetUseDevice(self):
        pass

    def SetUseDraft(self):
        pass

    def SetUseImageSequence(self):
        pass

    def SetUseIterative(self):
        pass

    def SetUseNet(self):
        pass

    def SetUsePostScript(self):
        pass

    def SetUsePreScript(self):
        pass

    def SetViewID(self):
        pass

    def SetWidth(self):
        pass

    def ShouldContinueOnError(self):
        pass

    def UpdateDialogParameters(self):
        pass


class RendParams(Wrapper):
    kCommand_IsToneOpPreview = 0
    RM_Default = 0
    RM_IReshade = 0

    def GetAlphaOutOnAdditive(self):
        pass

    def GetAtmos(self):
        pass

    def GetColorCheck(self):
        pass

    def GetComputeRadiosity(self):
        pass

    def GetDontAntialiasBG(self):
        pass

    def GetEffect(self):
        pass

    def GetEnvMap(self):
        pass

    def GetExtraFlags(self):
        pass

    def GetFieldOrder(self):
        pass

    def GetFieldRender(self):
        pass

    def GetFilterBG(self):
        pass

    def GetFirstFrame(self):
        pass

    def GetForce2Side(self):
        pass

    def GetFrameDur(self):
        pass

    def GetHeight(self):
        pass

    def GetInMtlEdit(self):
        pass

    def GetIsNetRender(self):
        pass

    def GetMtlEditAA(self):
        pass

    def GetMtlEditTile(self):
        pass

    def GetMultiThread(self):
        pass

    def GetNtscPAL(self):
        pass

    def GetPRadiosity(self):
        pass

    def GetPToneOp(self):
        pass

    def GetRendHidden(self):
        pass

    def GetRendType(self):
        pass

    def GetSbThresh(self):
        pass

    def GetScanBandHeight(self):
        pass

    def GetSimplifyAreaLights(self):
        pass

    def GetSuperBlack(self):
        pass

    def GetUseDisplacement(self):
        pass

    def GetUseEnvironAlpha(self):
        pass

    def GetUseRadiosity(self):
        pass

    def GetVidCorrectMethod(self):
        pass

    def GetWidth(self):
        pass

    def IsToneOperatorPreviewRender(self):
        pass

    def SetAlphaOutOnAdditive(self):
        pass

    def SetColorCheck(self):
        pass

    def SetComputeRadiosity(self):
        pass

    def SetDontAntialiasBG(self):
        pass

    def SetEffect(self):
        pass

    def SetEnvMap(self):
        pass

    def SetExtraFlags(self):
        pass

    def SetFieldOrder(self):
        pass

    def SetFieldRender(self):
        pass

    def SetFilterBG(self):
        pass

    def SetFirstFrame(self):
        pass

    def SetForce2Side(self):
        pass

    def SetFrameDur(self):
        pass

    def SetHeight(self):
        pass

    def SetInMtlEdit(self):
        pass

    def SetIsNetRender(self):
        pass

    def SetMtlEditAA(self):
        pass

    def SetMtlEditTile(self):
        pass

    def SetMultiThread(self):
        pass

    def SetNtscPAL(self):
        pass

    def SetRendHidden(self):
        pass

    def SetRendType(self):
        pass

    def SetSbThresh(self):
        pass

    def SetScanBandHeight(self):
        pass

    def SetSimplifyAreaLights(self):
        pass

    def SetSuperBlack(self):
        pass

    def SetUseDisplacement(self):
        pass

    def SetUseEnvironAlpha(self):
        pass

    def SetUseRadiosity(self):
        pass

    def SetVidCorrectMethod(self):
        pass

    def SetWidth(self):
        pass


class RendType:
    BakeAll = 0
    BakeSel = 0
    BakeSelCrop = 0
    BlowUp = 0
    BlowUpSel = 0
    CropSel = 0
    Normal = 0
    Region = 0
    RegionCrop = 0
    RegionSel = 0
    Select = 0


class ResCode:
    kRES_INTERNAL_ERROR = 0
    kRES_MOD_NOT_APPLICABLE = 0
    kRES_MOD_NOT_FOUND = 0
    kRES_SUCCESS = 0


class ScaleValue(Wrapper):
    this = ()
    Q = ()
    S = ()
    def GetQ(self):
        pass

    def GetS(self):
        pass

    def SetQ(self):
        pass

    def SetS(self):
        pass


class SchematicViews:
    Close = ()

    CloseAll = ()

    FlushAll = ()

    GetCount = ()

    GetName = ()

    Open = ()

    thisown = ()

    UnFlushAll = ()

    ZoomSelected = ()

    def Close(self):
        pass

    def CloseAll(self):
        pass

    def FlushAll(self):
        pass

    def GetCount(self):
        pass

    def GetName(self):
        pass

    def Open(self):
        pass

    def UnFlushAll(self):
        pass

    def ZoomSelected(self):
        pass


class SelectionManager:
    ClearCurNamedSelSet = ()

    ClearNodeSelection = ()

    DeSelectNode = ()

    DeselectNodes = ()

    GetCount = ()

    GetCrossing = ()

    GetFrozen = ()

    GetNode = ()

    GetNodes = ()

    GetNumberSelectFilters = ()

    GetSelectFilter = ()

    GetSelectFilterName = ()

    GetSelectionWorldBox = ()

    NamedSelSetListChanged = ()

    Nodes = ()

    SelectNode = ()

    SelectNodes = ()

    SelectNodeTab = ()

    SetCurNamedSelSet = ()

    SetFrozen = ()

    SetSelectFilter = ()

    SetSelectionType = ()

    SetTestOnlyFrozen = ()

    thisown = ()

    def ClearCurNamedSelSet(self):
        pass

    def ClearNodeSelection(self):
        pass

    def DeSelectNode(self):
        pass

    def DeselectNodes(self):
        pass

    def GetCount(self):
        pass

    def GetCrossing(self):
        pass

    def GetFrozen(self):
        pass

    def GetNode(self):
        pass

    def GetNodes(self):
        pass

    def GetNumberSelectFilters(self):
        pass

    def GetSelectFilter(self):
        pass

    def GetSelectFilterName(self):
        pass

    def GetSelectionWorldBox(self):
        pass

    def NamedSelSetListChanged(self):
        pass

    def SelectNode(self):
        pass

    def SelectNodes(self):
        pass

    def SelectNodeTab(self):
        pass

    def SetCurNamedSelSet(self):
        pass

    def SetFrozen(self):
        pass

    def SetSelectFilter(self):
        pass

    def SetSelectionType(self):
        pass

    def SetTestOnlyFrozen(self):
        pass


class SetXFormPacket(Wrapper):
    this = ()


class Snaps:
    GetAngleSnapStatus = ()

    GetPercentSnapStatus = ()

    GetSnapActive = ()

    GetSnapAngle = ()

    GetSnapMode = ()

    GetSnapPercent = ()

    GetSnapState = ()

    GetSnapType = ()

    InvalidateOsnapdraw = ()

    SetSnapActive = ()

    SetSnapAngle = ()

    SetSnapMode = ()

    SetSnapPercent = ()

    SetSnapType = ()

    SnapAngle = ()

    SnapPercent = ()

    thisown = ()

    ToggleAngleSnap = ()

    TogglePercentSnap = ()

    def GetAngleSnapStatus(self):
        pass

    def GetPercentSnapStatus(self):
        pass

    def GetSnapActive(self):
        pass

    def GetSnapAngle(self):
        pass

    def GetSnapMode(self):
        pass

    def GetSnapPercent(self):
        pass

    def GetSnapState(self):
        pass

    def GetSnapType(self):
        pass

    def InvalidateOsnapdraw(self):
        pass

    def SetSnapActive(self):
        pass

    def SetSnapAngle(self):
        pass

    def SetSnapMode(self):
        pass

    def SetSnapPercent(self):
        pass

    def SetSnapType(self):
        pass

    def SnapAngle(self):
        pass

    def SnapPercent(self):
        pass

    def ToggleAngleSnap(self):
        pass

    def TogglePercentSnap(self):
        pass


# A single knot in a spline
class SplineKnot(Wrapper):
    this = ()

    def ClearFlag(self):
        pass

    def ClearNoSnap(self):
        pass

    def GetAux(self):
        pass

    def GetAux2(self):
        pass

    def GetAux3(self):
        pass

    def GetFlag(self):
        pass

    def GetFlags(self):
        pass

    def GetInAux(self):
        pass

    def GetInAux2(self):
        pass

    def GetInAux3(self):
        pass

    def GetInVec(self):
        pass

    def GetKtype(self):
        pass

    def GetLtype(self):
        pass

    def GetMatID(self):
        pass

    def GetOutAux(self):
        pass

    def GetOutAux2(self):
        pass

    def GetOutAux3(self):
        pass

    def GetOutVec(self):
        pass

    def Hide(self):
        pass

    def IsHidden(self):
        pass

    def IsNoSnap(self):
        pass

    def SetAux(self):
        pass

    def SetAux2(self):
        pass

    def SetAux3(self):
        pass

    def SetFlag(self):
        pass

    def SetInAux(self):
        pass

    def SetInAux2(self):
        pass

    def SetInAux3(self):
        pass

    def SetInVec(self):
        pass

    def SetKnot(self):
        pass

    def SetKtype(self):
        pass

    def SetLtype(self):
        pass

    def SetMatID(self):
        pass

    def SetNoSnap(self):
        pass

    def SetOutAux(self):
        pass

    def SetOutAux2(self):
        pass

    def SetOutAux3(self):
        pass

    def SetOutVec(self):
        pass

    def Unhide(self):
        pass


class SplinePoint(Wrapper):
    this = ()

    def CopyFrom(self):
        pass

    def GetAux(self):
        pass

    def GetPoint(self):
        pass

    def SetAux(self):
        pass

    def SetPoint(self):
        pass


class SplineShape(ShapeObject):
    thisown = ()

    def CopyFrom(self):
        pass

    def GetShape(self):
        pass


class StatusPanel:
    DisableStatusXYZ = ()

    DisplayTempPrompt = ()

    EnableStatusXYZ = ()

    GetPrompt = ()

    PopPrompt = ()

    ProgressEnd = ()

    ProgressStart = ()

    ProgressUpdate = ()

    PushPrompt = ()

    RemoveTempPrompt = ()

    RepaintTimeSlider = ()

    ReplacePrompt = ()

    SetStatusXYZ = ()

    thisown = ()

    def DisableStatusXYZ(self):
        pass

    def DisplayTempPrompt(self):
        pass

    def EnableStatusXYZ(self):
        pass

    def GetPrompt(self):
        pass

    def PopPrompt(self):
        pass

    def ProgressEnd(self):
        pass

    def ProgressStart(self):
        pass

    def ProgressUpdate(self):
        pass

    def PushPrompt(self):
        pass

    def RemoveTempPrompt(self):
        pass

    def RepaintTimeSlider(self):
        pass

    def ReplacePrompt(self):
        pass

    def SetStatusXYZ(self):
        pass


class StdMat(Mtl):
    FaceMap = ()

    FalloffOut = ()

    Filter = ()

    IOR = ()

    LockAmbDiffTex = ()

    Opacity = ()

    OpacityFalloff = ()

    SamplingOn = ()

    SelfIllum = ()

    Shading = ()

    ShinyStrength = ()

    Soften = ()

    thisown = ()

    TransparencyType = ()

    TwoSided = ()

    Wire = ()

    WireSize = ()

    WireUnits = ()

    def GetFaceMap(self):
        pass

    def GetFalloffOut(self):
        pass

    def GetFilter(self):
        pass

    def GetIOR(self):
        pass

    def GetLockAmbDiffTex(self):
        pass

    def GetMapEnabled(self):
        pass

    def GetMapName(self):
        pass

    def GetMapState(self):
        pass

    def GetOpacFalloff(self):
        pass

    def GetOpacity(self):
        pass

    def GetReflectionDim(self):
        pass

    def GetSamplingOn(self):
        pass

    def GetSelfIllum(self):
        pass

    def GetSelfIllumColor(self):
        pass

    def GetSelfIllumColorOn(self):
        pass

    def GetShading(self):
        pass

    def GetShinyStrength(self):
        pass

    def GetSoften(self):
        pass

    def GetTexmapAmt(self):
        pass

    def GetTransparencyType(self):
        pass

    def GetTwoSided(self):
        pass

    def GetWire(self):
        pass

    def GetWireSize(self):
        pass

    def GetWireUnits(self):
        pass

    def IsFaceted(self):
        pass

    def KeyAtTimeByID(self):
        pass

    def SetEnableMap(self):
        pass

    def SetFaceMap(self):
        pass

    def SetFaceted(self):
        pass

    def SetFalloffOut(self):
        pass

    def SetFilter(self):
        pass

    def SetIOR(self):
        pass

    def SetLockAmbDiffTex(self):
        pass

    def SetOpacFalloff(self):
        pass

    def SetOpacity(self):
        pass

    def SetSamplingOn(self):
        pass

    def SetSelfIllum(self):
        pass

    def SetSelfIllumColor(self):
        pass

    def SetSelfIllumColorOn(self):
        pass

    def SetShading(self):
        pass

    def SetShinyStrength(self):
        pass

    def SetSoften(self):
        pass

    def SetTexmapAmt(self):
        pass

    def SetTransparencyType(self):
        pass

    def SetTwoSided(self):
        pass

    def SetWire(self):
        pass

    def SetWireSize(self):
        pass

    def SetWireUnits(self):
        pass

    def StdIDToChannel(self):
        pass

    def SupportsShaders(self):
        pass

    def SwitchSampler(self):
        pass

    def SwitchShader(self):
        pass

    def SyncADTexLock(self):
        pass

    def TranspColor(self):
        pass


class StrList:
    this = 0
    thisown = ()

    def Append(self):
        pass

    def Delete(self):
        pass

    def GetCount(self):
        pass

    def GetItem(self):
        pass

    def Insert(self):
        pass

    def SetCount(self):
        pass

    def SetItem(self):
        pass


class SuperClassIds:
    AggMan = 0
    AssignRef = 0
    Atmospheric = 0
    AxisDisplay = 0
    BaseNode = 0
    BezFont = 0
    BitmapDragAndDrop = 0
    BmmColorcut = 0
    BmmDiter = 0
    BmmFilter = 0
    BmmIO = 0
    BmmStorage = 0
    Camera = 0
    ColorPicker = 0
    ControllerFloat = 0
    ControllerMasterblock = 0
    ControllerMasterpoint = 0
    ControllerMatrix3 = 0
    ControllerMorph = 0
    ControllerPoint2 = 0
    ControllerPoint3 = 0
    ControllerPoint4 = 0
    ControllerPosition = 0
    ControllerRotation = 0
    ControllerScale = 0
    ControllerUsertype = 0
    DelRefRest = 0
    DerivedObject = 0
    EaseList = 0
    Export = 0
    FilterKernel = 0
    Flt = 0
    GenDerivedObject = 0
    GenModApp = 0
    GeomObject = 0
    GridRef = 0
    Gup = 0
    Helper = 0
    Import = 0
    Layer = 0
    Light = 0
    MakeRefRest = 0
    Material = 0
    MoCapDevice = 0
    MoCapDeviceBInding = 0
    ModApp = 0
    MSWrapper = 0
    MultiList = 0
    NoteTrack = 0
    ObjectRefModApp = 0
    Osm = 0
    OSnap = 0
    ParamBlock = 0
    ParamBlock2 = 0
    ParticleSys = 0
    RefMaker = 0
    RenderEffect = 0
    RenderElement = 0
    Renderer = 0
    Sampler = 0
    Scene = 0
    SchematicViewUtility = 0
    Shader = 0
    ShadowGenerator = 0
    Shape = 0
    SoundObj = 0
    System = 0
    Texmap = 0
    TexMapContainer = 0
    TexOutput = 0
    thisown = ()
    Trackbar = 0
    TrackView = 0
    TreeView = 0
    UserDataType = 0
    Utility = 0
    UVGen = 0
    ViewRef = 0
    Wsm = 0
    WsmDerivedObject = 0
    WSMObject = 0
    XYZGen = 0



class SwigPyIterator:
    thisown = ()
    def advance(self):
        pass

    def copy(self):
        pass

    def decr(self):
        pass

    def distance(self):
        pass

    def equal(self):
        pass

    def incr(self):
        pass

    def next(self):
        pass

    def previous(self):
        pass

    def value(self):
        pass


class Texmap(MtlBase):
    thisown = ()

    def GetHandlesOwnViewPerturb(self):
        return True

    def GetMapChannel(self):
        return 0

    def GetTextureTiling(self):
        return 0

    def GetUVTransform(self, Matrix3):
        pass

    def GetUVWSource(self):
        return 0

    def InitSlotType(self, int):
        pass

    def IsHighDynamicRange(self):
        return 0

    def LoadMapFiles(self, TimeValue):
        return 0

    def MapSlotType(self, int):
        return 0

    def RecurseInitSlotType(self, int):
        pass

    def RenderBitmap(self, Bitmap, scale3D):
        pass

    def SetOutputLevel(self, float, TimeValue):
        pass


class TexmapList:
    this = 0
    thisown = ()

    def Append(self):
        pass

    def Delete(self):
        pass

    def GetCount(self):
        pass

    def GetItem(self):
        pass

    def Insert(self):
        pass

    def SetCount(self):
        pass

    def SetItem(self):
        pass


class TextureOutput(MtlBase):
    thisown = ()

    def Filter(self):
        pass

    def GetInvert(self):
        pass

    def GetOutputLevel(self):
        pass

    def GetRollupOpen(self):
        pass

    def SetInvert(self):
        pass

    def SetOutputLevel(self):
        pass

    def SetRollupOpen(self):
        pass


class ToneOperator(SpecialFX):
    thisown = ()

    def CanInvert(self):
        pass

    def GetActive(self):
        pass

    def GetIndirectOnly(self):
        pass

    def GetPhysicalUnit(self):
        pass

    def GetProcessBackground(self):
        pass

    def IsPhysicalSpace(self):
        pass

    def RGBToScaled(self):
        pass

    def ScaledToRGB(self):
        pass

    def ScalePhysical(self):
        pass

    def ScaleRGB(self):
        pass

    def SetActive(self):
        pass

    def SetIndirectOnly(self):
        pass

    def SetPhysicalUnit(self):
        pass

    def SetProcessBackground(self):
        pass

    def Update(self):
        pass


class TrackView:
    ClearFilter = ()

    Close = ()

    CloseAll = ()

    FlushAll = ()

    GetCount = ()

    GetName = ()

    Open = ()

    SendToTop = ()

    SetFilter = ()

    TestFilter = ()

    thisown = ()

    UnFlush = ()

    Zoom = ()

    ZoomSelected = ()

    def ClearFilter(self):
        pass

    def Close(self):
        pass

    def CloseAll(self):
        pass

    def FlushAll(self):
        pass

    def GetCount(self):
        pass

    def GetName(self):
        pass

    def Open(self):
        pass

    def SendToTop(self):
        pass

    def SetFilter(self):
        pass

    def TestFilter(self):
        pass

    def UnFlush(self):
        pass

    def Zoom(self):
        pass

    def ZoomSelected(self):
        pass


class TransformGizmos:
    Deactivate = ()

    GetEnabled = ()

    GetRestoreAxis = ()

    GetTransformMatrix = ()

    SetEnabled = ()

    SetRestoreAxis = ()

    thisown = ()

    def Deactivate(self):
        pass

    def GetEnabled(self):
        pass

    def GetRestoreAxis(self):
        pass

    def GetTransformMatrix(self):
        pass

    def SetEnabled(self):
        pass

    def SetRestoreAxis(self):
        pass


class TVFace(Wrapper):
    this = ()
    A = ()
    B = ()
    C = ()
    def GetA(self):
        pass

    def GetB(self):
        pass

    def GetC(self):
        pass

    def GetItem(self):
        pass

    def SetA(self):
        pass

    def SetAt(self):
        pass

    def SetB(self):
        pass

    def SetC(self):
        pass


#qff
class ViewportManager:
    ActivateTexture = ()
    DeactivateTexture = ()
    DisableSceneRedraw = ()
    DisplayActiveCameraViewWithMultiPassEffect = ()
    DisplayViewportConfigDialogPage = ()
    EnableSceneRedraw = ()
    ForceCompleteRedraw = ()
    GetActiveViewport = ()
    GetActiveViewportIndex = ()
    getActiveViewportLabel = ()
    GetActiveViewportRenderLevel = ()
    GetActiveViewportShowEdgeFaces = ()
    GetActiveViewportTransparencyLevel = ()
    GetBlowupRect = ()
    GetBlowupRect2 = ()
    GetCrossHairCur = ()
    GetDualPlanes = ()
    GetExtendedDisplayMode = ()
    GetImageAspectRatio = ()
    GetImportZoomExtents = ()
    GetLockImageAspectRatio = ()
    GetLockPixelAspectRatio = ()
    GetMoveModeType = ()
    GetNumViewports = ()
    GetPaintSelBrushSize = ()
    GetPerspMouseSpeed = ()
    GetPixelAspectRatio = ()
    GetRegionRect = ()
    GetRegionRect2 = ()
    GetRotationIncrement = ()
    GetViewport = ()
    GetViewportByID = ()
    GetViewportGridVisible = ()
    getViewportLabel = ()
    GetViewportLayout = ()
    InvalidateAllViewportRects = ()
    IsConstructionPlaneEdgeOnInView = ()
    IsSceneRedrawDisabled = ()
    IsViewportMaxed = ()
    MakeExtendedViewportActive = ()
    RedrawViewportsLater = ()
    RedrawViewportsNow = ()
    RedrawViews = ()
    ResetAllViews = ()
    SetActiveViewport = ()
    SetActiveViewportRenderLevel = ()
    SetActiveViewportShowEdgeFaces = ()
    SetActiveViewportTransparencyDisplay = ()
    SetActiveViewportTransparencyLevel = ()
    SetBlowupRect = ()
    SetBlowupRect2 = ()
    SetCrossHairCur = ()
    SetDualPlanes = ()
    SetExtendedDisplayMode = ()
    SetHWNDAsActiveViewport = ()
    SetImageAspectRatio = ()
    SetImportZoomExtents = ()
    SetLockImageAspectRatio = ()
    SetLockPixelAspectRatio = ()
    SetMoveModeType = ()
    SetPaintSelBrushSize = ()
    SetPerspMouseSpeed = ()
    SetPixelAspectRatio = ()
    SetRegionRect = ()
    SetRegionRect2 = ()
    SetRotationIncrement = ()
    SetViewportGridVisible = ()
    SetViewportLayout = ()
    SetViewportMax = ()
    thisown = ()
    ViewportInvalidate = ()
    ViewportInvalidateBkgImage = ()
    Viewports = ()
    ViewportZoomExtents = ()
    ZoomToBounds = ()

    def ActivateTexture(self):
        pass

    def DeactivateTexture(self):
        pass

    def DisableSceneRedraw(self):
        pass

    def DisplayActiveCameraViewWithMultiPassEffect(self):
        pass

    def DisplayViewportConfigDialogPage(self):
        pass

    def EnableSceneRedraw(self):
        pass

    def ForceCompleteRedraw(self):
        pass

    def GetActiveViewport(self):
        pass

    def GetActiveViewportIndex(self):
        pass

    def getActiveViewportLabel(self):
        pass

    def GetActiveViewportRenderLevel(self):
        pass

    def GetActiveViewportShowEdgeFaces(self):
        pass

    def GetActiveViewportTransparencyLevel(self):
        pass

    def GetBlowupRect(self):
        pass

    def GetBlowupRect2(self):
        pass

    def GetCrossHairCur(self):
        pass

    def GetDualPlanes(self):
        pass

    def GetExtendedDisplayMode(self):
        pass

    def GetHideByCategoryFlags(self):
        pass

    def GetImageAspectRatio(self):
        pass

    def GetImportZoomExtents(self):
        pass

    def GetLockImageAspectRatio(self):
        pass

    def GetLockPixelAspectRatio(self):
        pass

    def GetMoveModeType(self):
        pass

    def GetNumViewports(self):
        pass

    def GetPaintSelBrushSize(self):
        pass

    def GetPerspMouseSpeed(self):
        pass

    def GetPixelAspectRatio(self):
        pass

    def GetRegionRect(self):
        pass

    def GetRegionRect2(self):
        pass

    def GetRotationIncrement(self):
        pass

    def GetViewport(self):
        pass

    def GetViewportByID(self):
        pass

    def GetViewportGridVisible(self):
        pass

    def getViewportLabel(self):
        pass

    def GetViewportLayout(self):
        pass

    def InvalidateAllViewportRects(self):
        pass

    def IsConstructionPlaneEdgeOnInView(self):
        pass

    def IsSceneRedrawDisabled(self):
        pass

    def IsViewportMaxed(self):
        pass

    def MakeExtendedViewportActive(self):
        pass

    def RedrawViewportsLater(self):
        pass

    def RedrawViewportsNow(self):
        pass

    def RedrawViews(self):
        pass

    def ResetAllViews(self):
        pass

    def SetActiveViewport(self):
        pass

    def SetActiveViewportRenderLevel(self):
        pass

    def SetActiveViewportShowEdgeFaces(self):
        pass

    def SetActiveViewportTransparencyDisplay(self):
        pass

    def SetActiveViewportTransparencyLevel(self):
        pass

    def SetBlowupRect(self):
        pass

    def SetBlowupRect2(self):
        pass

    def SetCrossHairCur(self):
        pass

    def SetDualPlanes(self):
        pass

    def SetExtendedDisplayMode(self):
        pass

    def SetHideByCategoryFlags(self):
        pass

    def SetHWNDAsActiveViewport(self):
        pass

    def SetImageAspectRatio(self):
        pass

    def SetImportZoomExtents(self):
        pass

    def SetLockImageAspectRatio(self):
        pass

    def SetLockPixelAspectRatio(self):
        pass

    def SetMoveModeType(self):
        pass

    def SetPaintSelBrushSize(self):
        pass

    def SetPerspMouseSpeed(self):
        pass

    def SetPixelAspectRatio(self):
        pass

    def SetRegionRect(self):
        pass

    def SetRegionRect2(self):
        pass

    def SetRotationIncrement(self):
        pass

    def SetViewportGridVisible(self):
        pass

    def SetViewportLayout(self):
        pass

    def SetViewportMax(self):
        pass

    def ViewportInvalidate(self):
        pass

    def ViewportInvalidateBkgImage(self):
        pass

    def ViewportZoomExtents(self):
        pass

    def ZoomToBounds(self):
        pass


class ViewportsBackground:
    GetColor = ()

    GetColorController = ()

    GetFrameNumber = ()

    GetFrameRange = ()

    GetImageAnimate = ()

    GetImageAspect = ()

    GetImageAsset = ()

    GetOutOfRangeType = ()

    GetStartTime = ()

    GetSyncFrame = ()

    SetColor = ()

    SetColorController = ()

    SetFrameRange = ()

    SetImageAnimate = ()

    SetImageAspect = ()

    SetImageAsset = ()

    SetOutOfRangeType = ()

    SetStartTime = ()

    SetSyncFrame = ()

    thisown = ()

    def GetColor(self):
        pass

    def GetColorController(self):
        pass

    def GetFrameNumber(self):
        pass

    def GetFrameRange(self):
        pass

    def GetImageAnimate(self):
        pass

    def GetImageAspect(self):
        pass

    def GetImageAsset(self):
        pass

    def GetOutOfRangeType(self):
        pass

    def GetStartTime(self):
        pass

    def GetSyncFrame(self):
        pass

    def SetColor(self):
        pass

    def SetColorController(self):
        pass

    def SetFrameRange(self):
        pass

    def SetImageAnimate(self):
        pass

    def SetImageAspect(self):
        pass

    def SetImageAsset(self):
        pass

    def SetOutOfRangeType(self):
        pass

    def SetStartTime(self):
        pass

    def SetSyncFrame(self):
        pass


class Win32:
    GetCheckBox = ()

    GetMAXHWnd = ()

    GetStatusPanelHWnd = ()

    GetViewPortHWnd = ()

    IsHovering = ()

    IsThemeSupported = ()

    IsVistaAeroEnabled = ()

    MakeButton2State = ()

    MakeButton3State = ()

    RegisterDialogWindow = ()

    RevealInExplorer = ()

    Set3dsMaxAsParentWindow = ()

    SetCheckBox = ()

    thisown = ()

    UnRegisterDialogWindow = ()

    def GetCheckBox(self):
        pass

    def GetMAXHWnd(self):
        pass

    def GetStatusPanelHWnd(self):
        pass

    def GetViewPortHWnd(self):
        pass

    def IsHovering(self):
        pass

    def IsThemeSupported(self):
        pass

    def IsVistaAeroEnabled(self):
        pass

    def MakeButton2State(self):
        pass

    def MakeButton3State(self):
        pass

    def RegisterDialogWindow(self):
        pass

    def RevealInExplorer(self):
        pass

    def Set3dsMaxAsParentWindow(self):
        pass

    def SetCheckBox(self):
        pass

    def UnRegisterDialogWindow(self):
        pass


class WStr(Wrapper):
    MatchPattern = ()

    MaxAlphaNumCompare = ()

    MaxAlphaNumCompareNoCase = ()

    def MatchPattern(self):
        pass

    def MaxAlphaNumCompare(self):
        pass

    def MaxAlphaNumCompareNoCase(self):
        pass


class XRefs:
    GetIncludeInHierarchy = ()

    IsAutoUpdateSuspended = ()

    SceneSetIgnoreFlag = ()

    SetAutoUpdateSuspended = ()

    SetIncludeInHierarchy = ()

    thisown = ()

    UpdateSceneXRefState = ()

    def GetIncludeInHierarchy(self):
        pass

    def IsAutoUpdateSuspended(self):
        pass

    def SceneSetIgnoreFlag(self):
        pass

    def SetAutoUpdateSuspended(self):
        pass

    def SetIncludeInHierarchy(self):
        pass

    def UpdateSceneXRefState(self):
        pass


####################################################################################################
# Functions
def AColor_AComp():
    pass


def AColor_CompositeOver():
    pass


def ActionContext__CastFrom():
    pass


def ActionItem__CastFrom():
    pass


def ActionManager_FindContext():
    pass


def ActionManager_GetActionContext():
    pass


def ActionManager_GetActionTable():
    pass


def ActionManager_GetFPStaticInterface():
    pass


def ActionManager_GetKeyboardFile():
    pass


def ActionManager_GetNumActionContexts():
    pass


def ActionManager_GetNumActionTables():
    pass


def ActionManager_GetShortcutDir():
    pass


def ActionManager_GetShortcutFile():
    pass


def ActionManager_IdToIndex():
    pass


def ActionManager_IsContextActive():
    pass


def ActionManager_LoadKeyboardFile():
    pass


def ActionManager_MakeActionSetCurrent():
    pass


def ActionManager_RegisterActionContext():
    pass


def ActionManager_SaveAllContextsToINI():
    pass


def ActionManager_SaveKeyboardFile():
    pass


def ActionTable__CastFrom():
    pass


def Animatable__CastFrom():
    pass


def Animatable_ClearFlagInAllAnimatables():
    pass


def Animatable_GetAnimByHandle():
    pass


def Animation_AreWeKeying():
    pass


def Animation_EnableAnimateButton():
    pass


def Animation_EndPlayback():
    pass


def Animation_GetAnimRange():
    pass


def Animation_GetAutoKeyDefaultKeyOn():
    pass


def Animation_GetAutoKeyDefaultKeyTime():
    pass


def Animation_GetControllerOverrideRangeDefault():
    pass


def Animation_GetDefaultInTangentType():
    pass


def Animation_GetDefaultOutTangentType():
    pass


def Animation_GetEndTime():
    pass


def Animation_GetIsAnimating():
    pass


def Animation_GetPlayActiveOnly():
    pass


def Animation_GetPlaybackLoop():
    pass


def Animation_GetPlaybackSpeed():
    pass


def Animation_GetRealTimePlayback():
    pass


def Animation_GetSetKeyMode():
    pass


def Animation_GetSetKeyModeStatus():
    pass


def Animation_GetSetKeySuspended():
    pass


def Animation_GetStartTime():
    pass


def Animation_GetTime():
    pass


def Animation_IsAnimateEnabled():
    pass


def Animation_IsPlaying():
    pass


def Animation_IsSetKeyModeFeatureEnabled():
    pass


def Animation_ResumeAnimate():
    pass


def Animation_ResumeSetKeyMode():
    pass


def Animation_SetAnimateButtonState():
    pass


def Animation_SetAutoKeyDefaultKeyOn():
    pass


def Animation_SetAutoKeyDefaultKeyTime():
    pass


def Animation_SetControllerOverrideRangeDefault():
    pass


def Animation_SetDefaultTangentType():
    pass


def Animation_SetEndTime():
    pass


def Animation_SetIsAnimating():
    pass


def Animation_SetPlayActiveOnly():
    pass


def Animation_SetPlaybackLoop():
    pass


def Animation_SetPlaybackSpeed():
    pass


def Animation_SetRange():
    pass


def Animation_SetRealTimePlayback():
    pass


def Animation_SetSetKeyMode():
    pass


def Animation_SetStartTime():
    pass


def Animation_SetTime():
    pass


def Animation_StartPlayback():
    pass


def Animation_SuspendAnimate():
    pass


def Animation_SuspendSetKeyMode():
    pass


def AnimationKeySteps_GetPosition():
    pass


def AnimationKeySteps_GetRotation():
    pass


def AnimationKeySteps_GetScale():
    pass


def AnimationKeySteps_GetSelectedOnly():
    pass


def AnimationKeySteps_GetUseTrackBar():
    pass


def AnimationKeySteps_GetUseTransform():
    pass


def AnimationKeySteps_SetPosition():
    pass


def AnimationKeySteps_SetRotation():
    pass


def AnimationKeySteps_SetScale():
    pass


def AnimationKeySteps_SetSelectedOnly():
    pass


def AnimationKeySteps_SetUseTrackBar():
    pass


def AnimationKeySteps_SetUseTransform():
    pass


def AnimationTrajectory_DeleteSelectedKey():
    pass


def AnimationTrajectory_GetAddKeyMode():
    pass


def AnimationTrajectory_GetKeySubMode():
    pass


def AnimationTrajectory_GetMode():
    pass


def AnimationTrajectory_SetAddKeyMode():
    pass


def AnimationTrajectory_SetKeySubMode():
    pass


def AnimationTrajectory_SetMode():
    pass


def Application_AutoBackupEnabled():
    pass


def Application_CheckMAXMessages():
    pass


def Application_DrawingEnabled():
    pass


def Application_EnableAutoBackup():
    pass


def Application_EnableDrawing():
    pass


def Application_ExecuteMAXCommand():
    pass


def Application_FlushUndoBuffer():
    pass


def Application_Get3DSMAXVersion():
    pass


def Application_GetAppID():
    pass


def Application_GetAutoBackupTime():
    pass


def Application_GetInterface():
    pass


def Application_GetLicenseBehavior():
    pass


def Application_GetLicenseDaysLeft():
    pass


def Application_GetProductVersion():
    pass


def Application_GetQuietMode():
    pass


def Application_GetScreenHeight():
    pass


def Application_GetScreenWidth():
    pass


def Application_GetSoundObject():
    pass


def Application_IsDebugging():
    pass


def Application_IsFeatureLicensed():
    pass


def Application_IsNetworkLicense():
    pass


def Application_IsQuitingApp():
    pass


def Application_IsSceneResetting():
    pass


def Application_IsTrialLicense():
    pass


def Application_IsUsingProfileDirectories():
    pass


def Application_IsUsingRoamingProfiles():
    pass


def Application_NumberOfProcessors():
    pass


def Application_RescaleWorldUnits():
    pass


def Application_SetAutoBackupTime():
    pass


def Application_SetQuietMode():
    pass


def Application_SetSoundObject():
    pass


def ArrayParameter__CastFrom():
    pass


def ArrayParameter_GetValue_Typed():
    pass


def ArrayParameter_SetValue_Typed():
    pass


def AssetDirectories_Add():
    pass


def AssetDirectories_AddSession():
    pass


def AssetDirectories_Delete():
    pass


def AssetDirectories_DeleteSession():
    pass


def AssetDirectories_Get():
    pass


def AssetDirectories_GetCount():
    pass


def AssetDirectories_GetCurrent():
    pass


def AssetDirectories_GetCurrentCount():
    pass


def AssetDirectories_GetSession():
    pass


def AssetDirectories_GetSessionCount():
    pass


def AssetDirectories_UpdateSection():
    pass


def AssetManager_CreateAsset():
    pass


def AssetManager_GetAssets():
    pass


def Atmospheric__CastFrom():
    pass


def Atomspherics_Add():
    pass


def Atomspherics_Delete():
    pass


def Atomspherics_Edit():
    pass


def Atomspherics_Get():
    pass


def Atomspherics_GetCount():
    pass


def Atomspherics_Set():
    pass


def Axis_EnableConstraints():
    pass


def Axis_GetConstantRestriction():
    pass


def Axis_GetConstraints():
    pass


def Axis_GetCount():
    pass


def Axis_GetTransformAxis():
    pass


def Axis_GetTripodLocked():
    pass


def Axis_PopConstraints():
    pass


def Axis_PushConstraints():
    pass


def Axis_SetConstantRestriction():
    pass


def Axis_SetConstraints():
    pass


def Axis_SetLockTripods():
    pass


def BaseInterface__CastFrom():
    pass


def BaseInterfaceServer__CastFrom():
    pass


def BaseObject__CastFrom():
    pass


def BezierShape__CastFrom():
    pass


def BitArray_kMAX_LOCALBITS():
    pass


def Bitmap__CastFrom():
    pass


def Bitmap_ClampColor():
    pass


def Bitmap_ClampColorA():
    pass


def Bitmap_ScaleColor():
    pass


def Bitmap_ScaleColorA():
    pass


def BitmapInfo__CastFrom():
    pass


def BitmapManager_CanImport():
    pass


def BitmapManager_FreeSceneBitmaps():
    pass


def BitmapManager_GetImageInfo():
    pass


def BitmapManager_GetImageInfoDlg():
    pass


def BitmapManager_GetImageInputOptions():
    pass


def BitmapManager_GetSilentMode():
    pass


def BitmapManager_Load():
    pass


def BitmapManager_SelectDeviceInput():
    pass


def BitmapManager_SelectDeviceOutput():
    pass


def BitmapManager_SelectFileInputEx():
    pass


def BitmapManager_SelectFileOutput():
    pass


def BitmapManager_SetSilentMode():
    pass


def BitmapStorage__CastFrom():
    pass


def BitmapStorage_ClampColor():
    pass


def BitmapStorage_ClampColorA():
    pass


def BitmapStorage_ScaleColor():
    pass


def BitmapStorage_ScaleColorA():
    pass


def BitmapTex__CastFrom():
    pass


def CameraObject__CastFrom():
    pass


def CameraState__CastFrom():
    pass


def ClassDesc__CastFrom():
    pass


def Color_color_spline():
    pass


def Color_to_COLORREF():
    pass


def CommandPanel_GetCurEditObject():
    pass


def CommandPanel_GetIsOpen():
    pass


def CommandPanel_IsEditing():
    pass


def CommandPanel_ResumeEditing():
    pass


def CommandPanel_ResumeMotionEditing():
    pass


def CommandPanel_SetCurrentEditObject():
    pass


def CommandPanel_SetOpen():
    pass


def CommandPanel_SuspendEditing():
    pass


def CommandPanel_SuspendMotionEditing():
    pass


def ConstObject__CastFrom():
    pass


def ContainerManager_AsContainer():
    pass


def ContainerManager_AsContainerNode():
    pass


def ContainerManager_CreateContainer():
    pass


def ContainerManager_CreateInheritedContainer():
    pass


def ContainerManager_GetContainer():
    pass


def ContainerManager_IsContainerNode():
    pass


def ContainerManager_IsInContainer():
    pass


def ContainerObject__CastFrom():
    pass


def Control__CastFrom():
    pass


def CoordinateSystem_AddReferencedNode():
    pass


def CoordinateSystem_EnableCenter():
    pass


def CoordinateSystem_EnableReferenceSystem():
    pass


def CoordinateSystem_GetCenter():
    pass


def CoordinateSystem_GetCurrent():
    pass


def CoordinateSystem_GetReferenceNode():
    pass


def CoordinateSystem_GetReferenceSystem():
    pass


def CoordinateSystem_SetCenter():
    pass


def CoordinateSystem_SetReferenceSystem():
    pass


def Core_EvalMAXScript():
    pass


def Core_GetCOREInterface():
    pass


def Core_GetCOREInterfaceAt():
    pass


def Core_GetCurrentTime():
    pass


def Core_GetFPInterface():
    pass


def Core_GetFPInterfaceDesc():
    pass


def Core_GetInterface():
    pass


def Core_GetRootNode():
    pass


def Core_GetWindowHandle():
    pass


def Core_Print():
    pass


def Core_SetCurrentTime():
    pass


def Core_Write():
    pass


def Core_WriteLine():
    pass


def CUI_AreAcceleratorsEnabled():
    pass


def CUI_AreAllFloatersHidden():
    pass


def CUI_DisableAccelerators():
    pass


def CUI_DoUICustomization():
    pass


def CUI_EnableAccelerators():
    pass


def CUI_EnableToolButton():
    pass


def CUI_GetActionCommonIReshadeTableId():
    pass


def CUI_GetActionIReshadeContext():
    pass


def CUI_GetActionMainUIContext():
    pass


def CUI_GetActionMainUITableId():
    pass


def CUI_GetActionMaterialEditorContext():
    pass


def CUI_GetActionMaterialEditorTableId():
    pass


def CUI_GetActionScanlineIReshadeTableId():
    pass


def CUI_GetActionSchematicViewContext():
    pass


def CUI_GetActionSchematicViewTableId():
    pass


def CUI_GetActionTrackViewContext():
    pass


def CUI_GetActionTrackViewTableId():
    pass


def CUI_GetActionVideoPostContext():
    pass


def CUI_GetActionVideoPostTableId():
    pass


def CUI_GetCancel():
    pass


def CUI_GetExpertMode():
    pass


def CUI_GetFlyOffTime():
    pass


def CUI_GetToolButtonState():
    pass


def CUI_LoadCUI():
    pass


def CUI_LoadCUIConfig():
    pass


def CUI_ResetToFactoryDefaultCUI():
    pass


def CUI_RevertToBackupCUI():
    pass


def CUI_SaveCUIAs():
    pass


def CUI_SetCancel():
    pass


def CUI_SetExpertMode():
    pass


def CUI_SetFlyOffTime():
    pass


def CUI_SetToolButtonState():
    pass


def CUI_ShowCustomizeDialog():
    pass


def CUI_WriteCUIConfig():
    pass


def CUIFrame__CastFrom():
    pass


def CUIFrame_Create():
    pass


def CUIFrameMgr_DrawCUIWindows():
    pass


def CUIFrameMgr_GetConfigFile():
    pass


def CUIFrameMgr_GetCount():
    pass


def CUIFrameMgr_GetCUIDirectory():
    pass


def CUIFrameMgr_GetFrame():
    pass


def CUIFrameMgr_RecalcLayout():
    pass


def CUIFrameMgr_ResetIconImages():
    pass


def CUIFrameMgr_SetConfigFile():
    pass


def CUIFrameMgr_SetMacroButtonStates():
    pass


def CustomAttribute__CastFrom():
    pass


def CustomAttributeContainer__CastFrom():
    pass


def DisplayFilters_GetCount():
    pass


def DisplayFilters_GetEnabled():
    pass


def DisplayFilters_GetHideFrozen():
    pass


def DisplayFilters_GetName():
    pass


def DisplayFilters_GetSceneDisplayFlag():
    pass


def DisplayFilters_IsNodeVisible():
    pass


def DisplayFilters_SetEnabled():
    pass


def DisplayFilters_SetSceneDisplayFlag():
    pass


def DummyObject__CastFrom():
    pass


def Effect__CastFrom():
    pass


def Effects_Add():
    pass


def Effects_CloseDialog():
    pass


def Effects_Delete():
    pass


def Effects_Edit():
    pass


def Effects_Get():
    pass


def Effects_GetCount():
    pass


def Effects_OpenDialog():
    pass


def Effects_Set():
    pass


def Environment_AddLightToScene():
    pass


def Environment_GetAmbient():
    pass


def Environment_GetAmbientController():
    pass


def Environment_GetLightConeConstraint():
    pass


def Environment_GetLightLevel():
    pass


def Environment_GetLightLevelController():
    pass


def Environment_GetLightTint():
    pass


def Environment_GetLightTintController():
    pass


def Environment_GetMap():
    pass


def Environment_GetMapEnabled():
    pass


def Environment_SetAmbient():
    pass


def Environment_SetAmbientController():
    pass


def Environment_SetLightLevel():
    pass


def Environment_SetLightLevelController():
    pass


def Environment_SetLightTint():
    pass


def Environment_SetLightTintController():
    pass


def Environment_SetMap():
    pass


def Environment_SetMapEnabled():
    pass


def Face__CastFrom():
    pass


def Factory_CreateAnimatable():
    pass


def Factory_CreateAtmospheric():
    pass


def Factory_CreateBitmap():
    pass


def Factory_CreateBoxGizmoObject():
    pass


def Factory_CreateCamera():
    pass


def Factory_CreateCameraObject():
    pass


def Factory_CreateCylGizmoObject():
    pass


def Factory_CreateDefaultBitmapTex():
    pass


def Factory_CreateDefaultBoolController():
    pass


def Factory_CreateDefaultColorController():
    pass


def Factory_CreateDefaultCompositeTex():
    pass


def Factory_CreateDefaultFloatController():
    pass


def Factory_CreateDefaultFRGBAController():
    pass


def Factory_CreateDefaultMasterPointController():
    pass


def Factory_CreateDefaultMatrix3Controller():
    pass


def Factory_CreateDefaultMixTex():
    pass


def Factory_CreateDefaultMultiMtl():
    pass


def Factory_CreateDefaultPoint2Controller():
    pass


def Factory_CreateDefaultPoint3Controller():
    pass


def Factory_CreateDefaultPoint4Controller():
    pass


def Factory_CreateDefaultPositionController():
    pass


def Factory_CreateDefaultRotationController():
    pass


def Factory_CreateDefaultScaleController():
    pass


def Factory_CreateDefaultSoundObj():
    pass


def Factory_CreateDefaultStdCubic():
    pass


def Factory_CreateDefaultStdFog():
    pass


def Factory_CreateDefaultStdMat():
    pass


def Factory_CreateDefaultStdMirror():
    pass


def Factory_CreateDefaultTintTex():
    pass


def Factory_CreateDerivedObject():
    pass


def Factory_CreateDirectionalLight():
    pass


def Factory_CreateDummyObject():
    pass


def Factory_CreateFloatController():
    pass


def Factory_CreateFreeCamera():
    pass


def Factory_CreateGeomObject():
    pass


def Factory_CreateGizmoObject():
    pass


def Factory_CreateHelperObject():
    pass


def Factory_CreateInterpFloat():
    pass


def Factory_CreateInterpPoint2():
    pass


def Factory_CreateInterpPoint3():
    pass


def Factory_CreateInterpPoint4():
    pass


def Factory_CreateInterpPosition():
    pass


def Factory_CreateInterpRotation():
    pass


def Factory_CreateInterpScale():
    pass


def Factory_CreateLight():
    pass


def Factory_CreateLightObject():
    pass


def Factory_CreateLookatControl():
    pass


def Factory_CreateMasterPointControl():
    pass


def Factory_CreateMaterial():
    pass


def Factory_CreateMatrix3Controller():
    pass


def Factory_CreateMorphController():
    pass


def Factory_CreateNewMesh():
    pass


def Factory_CreateNewTriObject():
    pass


def Factory_CreateNode():
    pass


def Factory_CreateObject():
    pass


def Factory_CreateObjectModifier():
    pass


def Factory_CreateOmniLight():
    pass


def Factory_CreateParallelCamera():
    pass


def Factory_CreatePoint3Controller():
    pass


def Factory_CreatePositionController():
    pass


def Factory_CreatePRSControl():
    pass


def Factory_CreateRenderElement():
    pass


def Factory_CreateRenderer():
    pass


def Factory_CreateRenderingEffect():
    pass


def Factory_CreateRotationController():
    pass


def Factory_CreateScaleController():
    pass


def Factory_CreateShapeObject():
    pass


def Factory_CreateSound():
    pass


def Factory_CreateSphereGizmoObject():
    pass


def Factory_CreateStorage():
    pass


def Factory_CreateTargetedCamera():
    pass


def Factory_CreateTargetedDirectionalLight():
    pass


def Factory_CreateTargetedSpotLight():
    pass


def Factory_CreateTargetObject():
    pass


def Factory_CreateTextureMap():
    pass


def Factory_CreateWorldSpaceModifier():
    pass


def Factory_CreateWSDerivedObject():
    pass


def Factory_GetDefaultController():
    pass


def Factory_IsCreatingObject():
    pass


def Factory_SetDefaultBoolController():
    pass


def Factory_SetDefaultColorController():
    pass


def Factory_SetDefaultController():
    pass


def Factory_SetDefaultFRGBAController():
    pass


def Factory_StartCreatingObject():
    pass


def Factory_StopCreating():
    pass


def FileManager_AppendToCurFilePath():
    pass


def FileManager_CanImportBitmap():
    pass


def FileManager_CanImportFile():
    pass


def FileManager_CheckForSave():
    pass


def FileManager_ChooseDirectory():
    pass


def FileManager_ConfigureBitmapPaths():
    pass


def FileManager_DoesFileExist():
    pass


def FileManager_DoMaxFileSaveAsDlg():
    pass


def FileManager_DownloadUrl():
    pass


def FileManager_Export():
    pass


def FileManager_ExportSelected():
    pass


def FileManager_Fetch():
    pass


def FileManager_GetFileName():
    pass


def FileManager_GetFileNameAndPath():
    pass


def FileManager_GetSaveRequiredFlag():
    pass


def FileManager_GetSavingVersion():
    pass


def FileManager_Hold():
    pass


def FileManager_Import():
    pass


def FileManager_IsAutoSaveRequired():
    pass


def FileManager_IsInternetCachedFile():
    pass


def FileManager_IsMaxFile():
    pass


def FileManager_IsSaveRequired():
    pass


def FileManager_IsSavingToFile():
    pass


def FileManager_Merge():
    pass


def FileManager_Open():
    pass


def FileManager_Reset():
    pass


def FileManager_Save():
    pass


def FileManager_SaveAs():
    pass


def FileManager_SaveNodes():
    pass


def FileManager_SaveNodesAsVersion():
    pass


def FileManager_SaveSceneAsVersion():
    pass


def FileManager_SaveSelected():
    pass


def FileManager_SaveSelectedNodesAsVersion():
    pass


def FileManager_SetSaveRequiredFlag():
    pass


def FileManager_SetSavingVersion():
    pass


def FilterKernel__CastFrom():
    pass


def Forever():
    pass


def FPInterface__CastFrom():
    pass


def FPInterfaceDesc__CastFrom():
    pass


def FPStaticInterface__CastFrom():
    pass


def FPTypeGetName(FPValue):
    return ''


def FPValue_Get():
    pass


def FrameRendParams__CastFrom():
    pass


def GammaMgr_DeGammaCorrect():
    pass


def GammaMgr_DisplayGammaCorrect():
    pass


def GammaMgr_Enable():
    pass


def GammaMgr_GammaCorrect():
    pass


def GammaMgr_GetDisplayGamma():
    pass


def GammaMgr_GetDitherPaletted():
    pass


def GammaMgr_GetDitherTrue():
    pass


def GammaMgr_GetFileInGamma():
    pass


def GammaMgr_GetFileOutGamma():
    pass


def GammaMgr_IsEnabled():
    pass


def GammaMgr_SetDisplayGamma():
    pass


def GammaMgr_SetDitherPaletted():
    pass


def GammaMgr_SetDitherTrue():
    pass


def GammaMgr_SetFileInGamma():
    pass


def GammaMgr_SetFileOutGamma():
    pass


def GenCamera__CastFrom():
    pass


def GenLight__CastFrom():
    pass


def GeomObject__CastFrom():
    pass


def GizmoObject__CastFrom():
    pass


def Grid_Add():
    pass


def Grid_GetActive():
    pass


def Grid_GetIntensity():
    pass


def Grid_GetMajorLines():
    pass


def Grid_GetSpacing():
    pass


def Grid_GetUseGridColor():
    pass


def Grid_GetWhiteOrigin():
    pass


def Grid_SetActive():
    pass


def Grid_SetIntensity():
    pass


def Grid_SetMajorLines():
    pass


def Grid_SetSpacing():
    pass


def Grid_SetUseGridColor():
    pass


def Grid_SetWhiteOrigin():
    pass


def HDRColor_ClipColor():
    pass


def HelperObject__CastFrom():
    pass


def ICustomControl__CastFrom():
    pass


def Identity():
    pass


def IDerivedObject__CastFrom():
    pass


def IMultiPassCameraEffect__CastFrom():
    pass


def INode__CastFrom():
    pass


def INode_AttachNodesToGroup():
    pass


def INode_CloseGroup():
    pass


def INode_DeleteNodes():
    pass


def INode_DetachNodesFromGroup():
    pass


def INode_ExplodeNodes():
    pass


def INode_FindNodeFromBaseObject():
    pass


def INode_FlashNodes():
    pass


def INode_GetAffectChildren():
    pass


def INode_GetINodeByHandle():
    pass


def INode_GetINodeByName():
    pass


def INode_GetINodeFromRenderID():
    pass


def INode_GetPivotMode():
    pass


def INode_GroupNodes():
    pass


def INode_NodeColorPicker():
    pass


def INode_OpenGroup():
    pass


def INode_SetAffectChildren():
    pass


def INode_SetNodeAttribute():
    pass


def INode_SetPivotMode():
    pass


def INode_UngroupNodes():
    pass


def InterfaceServer__CastFrom():
    pass


def IObject__CastFrom():
    pass


def IParamArray__CastFrom():
    pass


def IParamBlock2__CastFrom():
    pass


def IParamBlock__CastFrom():
    pass


def IParamMap__CastFrom():
    pass


def IScanRenderer__CastFrom():
    pass


def ISubMap__CastFrom():
    pass


def Layer__CastFrom():
    pass


def LayerManager_AddLayer():
    pass


def LayerManager_CreateLayer():
    pass


def LayerManager_DeleteLayer():
    pass


def LayerManager_DoLayerPropDialog():
    pass


def LayerManager_EditLayer():
    pass


def LayerManager_GetCurrentLayer():
    pass


def LayerManager_GetLayer():
    pass


def LayerManager_GetNumLayers():
    pass


def LayerManager_GetPropagateToLayer():
    pass


def LayerManager_GetRootLayer():
    pass


def LayerManager_GetSavedLayer():
    pass


def LayerManager_Reset():
    pass


def LayerManager_SetCurrentLayer():
    pass


def LayerManager_SetPropagateToLayer():
    pass


def LightObject__CastFrom():
    pass


def LinearShape__CastFrom():
    pass


def MakeNameScripterCompatible():
    pass


def MaterialEditor_CloseMtlDlg():
    pass


def MaterialEditor_FindMtlNameInScene():
    pass


def MaterialEditor_FlushMtlDlg():
    pass


def MaterialEditor_GetActiveSlot():
    pass


def MaterialEditor_GetMtlDlgMode():
    pass


def MaterialEditor_GetNumSlots():
    pass


def MaterialEditor_IsMtlDlgShowing():
    pass


def MaterialEditor_IsMtlInstanced():
    pass


def MaterialEditor_LoadMaterialLibrary():
    pass


def MaterialEditor_OpenMtlDlg():
    pass


def MaterialEditor_PutMaterial():
    pass


def MaterialEditor_SaveMaterialLibrary():
    pass


def MaterialEditor_SetActiveSlot():
    pass


def MaterialEditor_SetMtlDlgMode():
    pass


def MaterialEditor_SetSlot():
    pass


def MaterialEditor_UnFlushMtlDlg():
    pass


def MaterialEditor_UpdateMtlEditorBrackets():
    pass


def MaterialLibrary__CastFrom():
    pass


def MaterialLibrary_FileOpenMatLib():
    pass


def MaterialLibrary_FileSaveAsMatLib():
    pass


def MaterialLibrary_FileSaveMatLib():
    pass


def MaterialLibrary_GetCurrentLibrary():
    pass


def MaterialLibrary_GetNumSceneMaterials():
    pass


def MaterialLibrary_GetSceneMaterial():
    pass


def MaterialLibrary_GetSceneMaterialLibrary():
    pass


def MaterialLibrary_LoadDefaultMaterialLibrary():
    pass


def MaterialManager_DoMaterialBrowseDlg():
    pass


def MaterialManager_GetMatLibFileName():
    pass


def MaterialManager_GetMtlSlot():
    pass


def MaterialManager_IsMtlOkForScene():
    pass


def MaterialManager_PutMtlToMtlEditor():
    pass


def Math_BasisFromZDir():
    pass


def Math_Bias():
    pass


def Math_BoxStep():
    pass


def Math_Clamp():
    pass


def Math_Gain():
    pass


def Math_Noise1():
    pass


def Math_Noise2():
    pass


def Math_Noise3():
    pass


def Math_Noise3DS():
    pass


def Math_Noise4():
    pass


def Math_SmoothStep():
    pass


def Math_SRamp():
    pass


def Math_Threshold():
    pass


def Math_Turbulence():
    pass


def Matrix3_GetIdentity():
    pass


def Menu__CastFrom():
    pass


def MenuElement__CastFrom():
    pass


def MenuItem__CastFrom():
    pass


def MenuManager__CastFrom():
    pass


def MenuManager_FindMenu():
    pass


def MenuManager_GetMainMenu():
    pass


def MenuManager_GetMenuFile():
    pass


def MenuManager_LoadMenuFile():
    pass


def MenuManager_MenuExists():
    pass


def MenuManager_SaveMenuFile():
    pass


def MenuManager_UnregisterMenu():
    pass


def Mesh__CastFrom():
    pass


def Mesh_AffectRegionFunction():
    pass


def Mesh_CombineMeshes():
    pass


def Mesh_GetDisplayBackFaceVertices():
    pass


def Mesh_GetHandleBoxType():
    pass


def Mesh_GetMapChannelID():
    pass


def Mesh_GetMapChannelNum():
    pass


def Mesh_GetUseVertexDots():
    pass


def Mesh_GetUseVisEdge():
    pass


def Mesh_GetVertexDotType():
    pass


def Mesh_SetDisplayBackFaceVertices():
    pass


def Mesh_SetHandleBoxType():
    pass


def Mesh_SetUseVertexDots():
    pass


def Mesh_SetUseVisEdge():
    pass


def Mesh_SetVertexDotType():
    pass


def Mesh_SliceMesh():
    pass


def Mesh_VertexDataType():
    pass


def ModContext__CastFrom():
    pass


def Modifier__CastFrom():
    pass


def ModifierPanel_Add():
    pass


def ModifierPanel_AddToSelection():
    pass


def ModifierPanel_Delete():
    pass


def ModifierPanel_EnableShowEndResult():
    pass


def ModifierPanel_GetContexts():
    pass


def ModifierPanel_GetReplaceableObjRef():
    pass


def ModifierPanel_GetShowEndResult():
    pass


def ModifierPanel_IsValid():
    pass


def ModifierPanel_SetShowEndResult():
    pass


def Mtl__CastFrom():
    pass


def Mtl_CombineMaterials():
    pass


def MtlBase__CastFrom():
    pass


def MultiMtl__CastFrom():
    pass


def Names_AssignNew():
    pass


def Names_GetSuffixLength():
    pass


def Names_MakeNodeNameUnique():
    pass


def Names_SetSuffixLength():
    pass


def NegInfinity():
    pass


def Never():
    pass


def Now():
    pass


def Object__CastFrom():
    pass


def OSModifier__CastFrom():
    pass


def ParamBlockDesc2__CastFrom():
    pass


def ParamDimension__CastFrom():
    pass


def ParamDimension_GetDefaultDim():
    pass


def ParamDimension_GetStdAngleDim():
    pass


def ParamDimension_GetStdColor255Dim():
    pass


def ParamDimension_GetStdColorDim():
    pass


def ParamDimension_GetStdNormalizedDim():
    pass


def ParamDimension_GetStdPercentDim():
    pass


def ParamDimension_GetStdSegmentsDim():
    pass


def ParamDimension_GetStdTimeDim():
    pass


def ParamDimension_GetStdWorldDim():
    pass


def ParamDimensionBase__CastFrom():
    pass


def Parameter__CastFrom():
    pass


def Parameter_GetValue_Typed():
    pass


def Parameter_SetValue_Typed():
    pass


def PathManager_GetAnimationDir():
    pass


def PathManager_GetAppExchangeStorePrivateDir():
    pass


def PathManager_GetAppExchangeStorePublicDir():
    pass


def PathManager_GetArchivesDir():
    pass


def PathManager_GetAutobackDir():
    pass


def PathManager_GetAutodeskCloudDir():
    pass


def PathManager_GetDownloadDir():
    pass


def PathManager_GetDriversDir():
    pass


def PathManager_GetExportDir():
    pass


def PathManager_GetExpressionDir():
    pass


def PathManager_GetFontDir():
    pass


def PathManager_GetHelpDir():
    pass


def PathManager_GetImageDir():
    pass


def PathManager_GetImportDir():
    pass


def PathManager_GetManagedAssembliesDir():
    pass


def PathManager_GetMarketDefaultsDir():
    pass


def PathManager_GetMatlibDir():
    pass


def PathManager_GetMaxdataDir():
    pass


def PathManager_GetMaxstartDir():
    pass


def PathManager_GetMaxSysRootDir():
    pass


def PathManager_GetNonLocalizedPluginCfg():
    pass


def PathManager_GetNonLocalizedUIDataDir():
    pass


def PathManager_GetPageFileDir():
    pass


def PathManager_GetPhotometricDir():
    pass


def PathManager_GetPlugcfgDir():
    pass


def PathManager_GetPreviewDir():
    pass


def PathManager_GetProjectFolderDir():
    pass


def PathManager_GetProxiesDir():
    pass


def PathManager_GetRenderAssetsDir():
    pass


def PathManager_GetRenderOutputDir():
    pass


def PathManager_GetRenderPresetsDir():
    pass


def PathManager_GetSceneDir():
    pass


def PathManager_GetScriptsDir():
    pass


def PathManager_GetShaderCacheDir():
    pass


def PathManager_GetSoundDir():
    pass


def PathManager_GetStartupscriptsDir():
    pass


def PathManager_GetTempDir():
    pass


def PathManager_GetUiDir():
    pass


def PathManager_GetUserIconsDir():
    pass


def PathManager_GetUserMacrosDir():
    pass


def PathManager_GetUserScriptsDir():
    pass


def PathManager_GetUserStartupscriptsDir():
    pass


def PathManager_GetVpostDir():
    pass


def PathManager_SetAnimationDir():
    pass


def PathManager_SetArchivesDir():
    pass


def PathManager_SetAutobackDir():
    pass


def PathManager_SetAutodeskCloudDir():
    pass


def PathManager_SetDownloadDir():
    pass


def PathManager_SetDriversDir():
    pass


def PathManager_SetExportDir():
    pass


def PathManager_SetExpressionDir():
    pass


def PathManager_SetFontDir():
    pass


def PathManager_SetHelpDir():
    pass


def PathManager_SetImageDir():
    pass


def PathManager_SetImportDir():
    pass


def PathManager_SetManagedAssembliesDir():
    pass


def PathManager_SetMarketDefaultsDir():
    pass


def PathManager_SetMatlibDir():
    pass


def PathManager_SetMaxdataDir():
    pass


def PathManager_SetMaxstartDir():
    pass


def PathManager_SetMaxSysRootDir():
    pass


def PathManager_SetNonLocalizedPluginCfg():
    pass


def PathManager_SetNonLocalizedUIDataDir():
    pass


def PathManager_SetPageFileDir():
    pass


def PathManager_SetPhotometricDir():
    pass


def PathManager_SetPlugcfgDir():
    pass


def PathManager_SetPreviewDir():
    pass


def PathManager_SetProjectFolderDir():
    pass


def PathManager_SetProxiesDir():
    pass


def PathManager_SetRenderAssetsDir():
    pass


def PathManager_SetRenderOutputDir():
    pass


def PathManager_SetRenderPresetsDir():
    pass


def PathManager_SetSceneDir():
    pass


def PathManager_SetScriptsDir():
    pass


def PathManager_SetShaderCacheDir():
    pass


def PathManager_SetSoundDir():
    pass


def PathManager_SetStartupscriptsDir():
    pass


def PathManager_SetTempDir():
    pass


def PathManager_SetUiDir():
    pass


def PathManager_SetUserIconsDir():
    pass


def PathManager_SetUserMacrosDir():
    pass


def PathManager_SetUserScriptsDir():
    pass


def PathManager_SetUserStartupscriptsDir():
    pass


def PathManager_SetVpostDir():
    pass


def PluginManager_GetClassInfo():
    pass


def PluginManager_GetClassList():
    pass


def PluginManager_GetNumClasses():
    pass


def PluginManager_GetNumPluginDlls():
    pass


def PluginManager_GetPluginDll():
    pass


def Point2_GetOrigin():
    pass


def Point2_GetXAxis():
    pass


def Point2_GetYAxis():
    pass


def Point3_GetOrigin():
    pass


def Point3_GetXAxis():
    pass


def Point3_GetYAxis():
    pass


def Point3_GetZAxis():
    pass


def Point4_GetOrigin():
    pass


def Point4_GetWAxis():
    pass


def Point4_GetXAxis():
    pass


def Point4_GetYAxis():
    pass


def Point4_GetZAxis():
    pass


def PolyLine__CastFrom():
    pass


def PolyObject__CastFrom():
    pass


def PolyShape__CastFrom():
    pass


def PosInfinity():
    pass


def PreferencesFileEncoding_CodePageForLanguage():
    pass


def PreferencesFileEncoding_DefaultTextLoadCodePage():
    pass


def PreferencesFileEncoding_DefaultTextSaveCodePage():
    pass


def PreferencesFileEncoding_LanguageToUseForFileIO():
    pass


def PreferencesFileEncoding_LegacyFilesCanBeStoredUsingUTF8():
    pass


def PreferencesFileEncoding_OverrideLanguageSpecifiedInSceneFile():
    pass


def PreferencesFileEncoding_SetLanguageToUseForFileIO():
    pass


def PreferencesFileEncoding_SetLegacyFilesCanBeStoredUsingUTF8():
    pass


def PreferencesFileEncoding_SetOverrideLanguageSpecifiedInSceneFile():
    pass


def PreferencesFileEncoding_SetUseCodePageSpecifiedInSceneFile():
    pass


def PreferencesFileEncoding_UseCodePageSpecifiedInSceneFile():
    pass


def PreferencesRendering_GetRendDither256():
    pass


def PreferencesRendering_GetRendDitherTrue():
    pass


def PreferencesRendering_GetRendFieldOrder():
    pass


def PreferencesRendering_GetRendMultiThread():
    pass


def PreferencesRendering_GetRendNThSerial():
    pass


def PreferencesRendering_GetRendNTSC_PAL():
    pass


def PreferencesRendering_GetRendSuperBlackThresh():
    pass


def PreferencesRendering_GetRendVidCorrectMethod():
    pass


def PreferencesRendering_SetRendDither256():
    pass


def PreferencesRendering_SetRendDitherTrue():
    pass


def PreferencesRendering_SetRendFieldOrder():
    pass


def PreferencesRendering_SetRendMultiThread():
    pass


def PreferencesRendering_SetRendNThSerial():
    pass


def PreferencesRendering_SetRendNTSC_PAL():
    pass


def PreferencesRendering_SetRendSuperBlackThresh():
    pass


def PreferencesRendering_SetRendVidCorrectMethod():
    pass


def PreviewParams_GetViewportPreview():
    pass


def QuadMenu__CastFrom():
    pass


def RadiosityEffect__CastFrom():
    pass


def RealWorldMapSizeInterface__CastFrom():
    pass


def ReferenceMaker__CastFrom():
    pass


def ReferenceTarget__CastFrom():
    pass


def RenderElement__CastFrom():
    pass


def RenderElementMgr__CastFrom():
    pass


def Renderer__CastFrom():
    pass


def RenderExecute_Close():
    pass


def RenderExecute_CloseCurrent():
    pass


def RenderExecute_CreatePreview():
    pass


def RenderExecute_Open():
    pass


def RenderExecute_QuickRender():
    pass


def RenderExecute_RenderFrame():
    pass


def RenderSettings_BeginProgressiveMode():
    pass


def RenderSettings_CancelDialog():
    pass


def RenderSettings_CloseDialog():
    pass


def RenderSettings_ColorById():
    pass


def RenderSettings_CommitDialogParameters():
    pass


def RenderSettings_CreateDefault():
    pass


def RenderSettings_CreateDefaultScanline():
    pass


def RenderSettings_DialogOpen():
    pass


def RenderSettings_EndProgressiveMode():
    pass


def RenderSettings_FormatRenderTime():
    pass


def RenderSettings_Get():
    pass


def RenderSettings_GetActualMEditRenderer():
    pass


def RenderSettings_GetApertureWidth():
    pass


def RenderSettings_GetAreaType():
    pass


def RenderSettings_GetAtmosphere():
    pass


def RenderSettings_GetCamera():
    pass


def RenderSettings_GetColorCheck():
    pass


def RenderSettings_GetCurrent():
    pass


def RenderSettings_GetCurrentRenderElementManager():
    pass


def RenderSettings_GetCurrentSetting():
    pass


def RenderSettings_GetDefaultRendererClassID():
    pass


def RenderSettings_GetDeviceBitmapInfo():
    pass


def RenderSettings_GetDisplacement():
    pass


def RenderSettings_GetDraft():
    pass


def RenderSettings_GetEffects():
    pass


def RenderSettings_GetEnd():
    pass


def RenderSettings_GetFileBitmapInfo():
    pass


def RenderSettings_GetFileNumberBase():
    pass


def RenderSettings_GetForce2Side():
    pass


def RenderSettings_GetFrameList():
    pass


def RenderSettings_GetHeight():
    pass


def RenderSettings_GetHidden():
    pass


def RenderSettings_GetImageAspectRatio():
    pass


def RenderSettings_GetImageSequenceType():
    pass


def RenderSettings_GetLastRenderedImage():
    pass


def RenderSettings_GetLocalPreScript():
    pass


def RenderSettings_GetMEditRenderer():
    pass


def RenderSettings_GetMEditRendererLocked():
    pass


def RenderSettings_GetMEditRendererLocked_Default():
    pass


def RenderSettings_GetNThFrame():
    pass


def RenderSettings_GetOutputFile():
    pass


def RenderSettings_GetPickFramesString():
    pass


def RenderSettings_GetPixelAspectRatio():
    pass


def RenderSettings_GetPostScriptFile():
    pass


def RenderSettings_GetPreScriptFile():
    pass


def RenderSettings_GetPresetCount():
    pass


def RenderSettings_GetPresetDisplayName():
    pass


def RenderSettings_GetPresetFileName():
    pass


def RenderSettings_GetProduction():
    pass


def RenderSettings_GetRenderElementMgr():
    pass


def RenderSettings_GetSaveFile():
    pass


def RenderSettings_GetShowVFB():
    pass


def RenderSettings_GetSimplifyAreaLights():
    pass


def RenderSettings_GetSkipFrames():
    pass


def RenderSettings_GetStart():
    pass


def RenderSettings_GetSuperBlack():
    pass


def RenderSettings_GetTimeType():
    pass


def RenderSettings_GetToFields():
    pass


def RenderSettings_GetUseActiveView():
    pass


def RenderSettings_GetUseDevice():
    pass


def RenderSettings_GetUseDraft():
    pass


def RenderSettings_GetUseImageSequence():
    pass


def RenderSettings_GetUseIterative():
    pass


def RenderSettings_GetUseNet():
    pass


def RenderSettings_GetUsePostScript():
    pass


def RenderSettings_GetUsePreScript():
    pass


def RenderSettings_GetViewID():
    pass


def RenderSettings_GetViewParamsFromNode():
    pass


def RenderSettings_GetWidth():
    pass


def RenderSettings_InProgressiveMode():
    pass


def RenderSettings_IsActive():
    pass


def RenderSettings_OpenDialog():
    pass


def RenderSettings_Set():
    pass


def RenderSettings_SetApertureWidth():
    pass


def RenderSettings_SetAreaType():
    pass


def RenderSettings_SetAtmosphere():
    pass


def RenderSettings_SetCamera():
    pass


def RenderSettings_SetColorCheck():
    pass


def RenderSettings_SetCurrent():
    pass


def RenderSettings_SetCurrentSetting():
    pass


def RenderSettings_SetDefaultRendererClassID():
    pass


def RenderSettings_SetDisplacement():
    pass


def RenderSettings_SetDraft():
    pass


def RenderSettings_SetEffects():
    pass


def RenderSettings_SetEnd():
    pass


def RenderSettings_SetFileNumberBase():
    pass


def RenderSettings_SetForce2Side():
    pass


def RenderSettings_SetHeight():
    pass


def RenderSettings_SetHidden():
    pass


def RenderSettings_SetImageSequenceType():
    pass


def RenderSettings_SetLocalPreScript():
    pass


def RenderSettings_SetMEditRenderer():
    pass


def RenderSettings_SetMEditRendererLocked():
    pass


def RenderSettings_SetMEditRendererLocked_Default():
    pass


def RenderSettings_SetNThFrame():
    pass


def RenderSettings_SetOutputFile():
    pass


def RenderSettings_SetPixelAspectRatio():
    pass


def RenderSettings_SetPostScriptFile():
    pass


def RenderSettings_SetPreScriptFile():
    pass


def RenderSettings_SetProduction():
    pass


def RenderSettings_SetSaveFile():
    pass


def RenderSettings_SetShowVFB():
    pass


def RenderSettings_SetSimplifyAreaLights():
    pass


def RenderSettings_SetSkipFrames():
    pass


def RenderSettings_SetStart():
    pass


def RenderSettings_SetSuperBlack():
    pass


def RenderSettings_SetTimeType():
    pass


def RenderSettings_SetToFields():
    pass


def RenderSettings_SetupParameters():
    pass


def RenderSettings_SetUseActiveView():
    pass


def RenderSettings_SetUseDevice():
    pass


def RenderSettings_SetUseDraft():
    pass


def RenderSettings_SetUseImageSequence():
    pass


def RenderSettings_SetUseIterative():
    pass


def RenderSettings_SetUseNet():
    pass


def RenderSettings_SetUsePostScript():
    pass


def RenderSettings_SetUsePreScript():
    pass


def RenderSettings_SetViewID():
    pass


def RenderSettings_SetWidth():
    pass


def RenderSettings_ShouldContinueOnError():
    pass


def RenderSettings_UpdateDialogParameters():
    pass


def SchematicViews_Close():
    pass


def SchematicViews_CloseAll():
    pass


def SchematicViews_FlushAll():
    pass


def SchematicViews_GetCount():
    pass


def SchematicViews_GetName():
    pass


def SchematicViews_Open():
    pass


def SchematicViews_UnFlushAll():
    pass


def SchematicViews_ZoomSelected():
    pass


def SecsToTicks():
    pass


def SelectionManager_ClearCurNamedSelSet():
    pass


def SelectionManager_ClearNodeSelection():
    pass


def SelectionManager_DeSelectNode():
    pass


def SelectionManager_DeselectNodes():
    pass


def SelectionManager_GetCount():
    pass


def SelectionManager_GetCrossing():
    pass


def SelectionManager_GetFrozen():
    pass


def SelectionManager_GetNode():
    pass


def SelectionManager_GetNodes():
    pass


def SelectionManager_GetNumberSelectFilters():
    pass


def SelectionManager_GetSelectFilter():
    pass


def SelectionManager_GetSelectFilterName():
    pass


def SelectionManager_GetSelectionWorldBox():
    pass


def SelectionManager_NamedSelSetListChanged():
    pass


def SelectionManager_SelectNode():
    pass


def SelectionManager_SelectNodes():
    pass


def SelectionManager_SelectNodeTab():
    pass


def SelectionManager_SetCurNamedSelSet():
    pass


def SelectionManager_SetFrozen():
    pass


def SelectionManager_SetSelectFilter():
    pass


def SelectionManager_SetSelectionType():
    pass


def SelectionManager_SetTestOnlyFrozen():
    pass


def ShapeObject__CastFrom():
    pass


def Snaps_GetAngleSnapStatus():
    pass


def Snaps_GetPercentSnapStatus():
    pass


def Snaps_GetSnapActive():
    pass


def Snaps_GetSnapAngle():
    pass


def Snaps_GetSnapMode():
    pass


def Snaps_GetSnapPercent():
    pass


def Snaps_GetSnapState():
    pass


def Snaps_GetSnapType():
    pass


def Snaps_InvalidateOsnapdraw():
    pass


def Snaps_SetSnapActive():
    pass


def Snaps_SetSnapAngle():
    pass


def Snaps_SetSnapMode():
    pass


def Snaps_SetSnapPercent():
    pass


def Snaps_SetSnapType():
    pass


def Snaps_SnapAngle():
    pass


def Snaps_SnapPercent():
    pass


def Snaps_ToggleAngleSnap():
    pass


def Snaps_TogglePercentSnap():
    pass


def SoundObj__CastFrom():
    pass


def SpecialFX__CastFrom():
    pass


def SplineShape__CastFrom():
    pass


def StatusPanel_DisableStatusXYZ():
    pass


def StatusPanel_DisplayTempPrompt():
    pass


def StatusPanel_EnableStatusXYZ():
    pass


def StatusPanel_GetPrompt():
    pass


def StatusPanel_PopPrompt():
    pass


def StatusPanel_ProgressEnd():
    pass


def StatusPanel_ProgressStart():
    pass


def StatusPanel_ProgressUpdate():
    pass


def StatusPanel_PushPrompt():
    pass


def StatusPanel_RemoveTempPrompt():
    pass


def StatusPanel_RepaintTimeSlider():
    pass


def StatusPanel_ReplacePrompt():
    pass


def StatusPanel_SetStatusXYZ():
    pass


def StdMat__CastFrom():
    pass


def swig_import_helper():
    pass


def Texmap__CastFrom():
    pass


def TextureOutput__CastFrom():
    pass


def TicksToSecs():
    pass


def ToneOperator__CastFrom():
    pass


def TrackView_ClearFilter():
    pass


def TrackView_Close():
    pass


def TrackView_CloseAll():
    pass


def TrackView_FlushAll():
    pass


def TrackView_GetCount():
    pass


def TrackView_GetName():
    pass


def TrackView_Open():
    pass


def TrackView_SendToTop():
    pass


def TrackView_SetFilter():
    pass


def TrackView_TestFilter():
    pass


def TrackView_UnFlush():
    pass


def TrackView_Zoom():
    pass


def TrackView_ZoomSelected():
    pass


def TransformGizmos_Deactivate():
    pass


def TransformGizmos_GetEnabled():
    pass


def TransformGizmos_GetRestoreAxis():
    pass


def TransformGizmos_GetTransformMatrix():
    pass


def TransformGizmos_SetEnabled():
    pass


def TransformGizmos_SetRestoreAxis():
    pass


def TriObject__CastFrom():
    pass


def TriObject_GetNumTriFaces():
    pass


def TriObject_GetNumTriVerts():
    pass


def ViewParams__CastFrom():
    pass


def Viewport__CastFrom():
    pass


def ViewportManager_ActivateTexture():
    pass


def ViewportManager_DeactivateTexture():
    pass


def ViewportManager_DisableSceneRedraw():
    pass


def ViewportManager_DisplayActiveCameraViewWithMultiPassEffect():
    pass


def ViewportManager_DisplayViewportConfigDialogPage():
    pass


def ViewportManager_EnableSceneRedraw():
    pass


def ViewportManager_ForceCompleteRedraw():
    pass


def ViewportManager_GetActiveViewport():
    pass


def ViewportManager_GetActiveViewportIndex():
    pass


def ViewportManager_getActiveViewportLabel():
    pass


def ViewportManager_GetActiveViewportRenderLevel():
    pass


def ViewportManager_GetActiveViewportShowEdgeFaces():
    pass


def ViewportManager_GetActiveViewportTransparencyLevel():
    pass


def ViewportManager_GetBlowupRect():
    pass


def ViewportManager_GetBlowupRect2():
    pass


def ViewportManager_GetCrossHairCur():
    pass


def ViewportManager_GetDualPlanes():
    pass


def ViewportManager_GetExtendedDisplayMode():
    pass


def ViewportManager_GetImageAspectRatio():
    pass


def ViewportManager_GetImportZoomExtents():
    pass


def ViewportManager_GetLockImageAspectRatio():
    pass


def ViewportManager_GetLockPixelAspectRatio():
    pass


def ViewportManager_GetMoveModeType():
    pass


def ViewportManager_GetNumViewports():
    pass


def ViewportManager_GetPaintSelBrushSize():
    pass


def ViewportManager_GetPerspMouseSpeed():
    pass


def ViewportManager_GetPixelAspectRatio():
    pass


def ViewportManager_GetRegionRect():
    pass


def ViewportManager_GetRegionRect2():
    pass


def ViewportManager_GetRotationIncrement():
    pass


def ViewportManager_GetViewport():
    pass


def ViewportManager_GetViewportByID():
    pass


def ViewportManager_GetViewportGridVisible():
    pass


def ViewportManager_getViewportLabel():
    pass


def ViewportManager_GetViewportLayout():
    pass


def ViewportManager_InvalidateAllViewportRects():
    pass


def ViewportManager_IsConstructionPlaneEdgeOnInView():
    pass


def ViewportManager_IsSceneRedrawDisabled():
    pass


def ViewportManager_IsViewportMaxed():
    pass


def ViewportManager_MakeExtendedViewportActive():
    pass


def ViewportManager_RedrawViewportsLater():
    pass


def ViewportManager_RedrawViewportsNow():
    pass


def ViewportManager_RedrawViews():
    pass


def ViewportManager_ResetAllViews():
    pass


def ViewportManager_SetActiveViewport():
    pass


def ViewportManager_SetActiveViewportRenderLevel():
    pass


def ViewportManager_SetActiveViewportShowEdgeFaces():
    pass


def ViewportManager_SetActiveViewportTransparencyDisplay():
    pass


def ViewportManager_SetActiveViewportTransparencyLevel():
    pass


def ViewportManager_SetBlowupRect():
    pass


def ViewportManager_SetBlowupRect2():
    pass


def ViewportManager_SetCrossHairCur():
    pass


def ViewportManager_SetDualPlanes():
    pass


def ViewportManager_SetExtendedDisplayMode():
    pass


def ViewportManager_SetHWNDAsActiveViewport():
    pass


def ViewportManager_SetImageAspectRatio():
    pass


def ViewportManager_SetImportZoomExtents():
    pass


def ViewportManager_SetLockImageAspectRatio():
    pass


def ViewportManager_SetLockPixelAspectRatio():
    pass


def ViewportManager_SetMoveModeType():
    pass


def ViewportManager_SetPaintSelBrushSize():
    pass


def ViewportManager_SetPerspMouseSpeed():
    pass


def ViewportManager_SetPixelAspectRatio():
    pass


def ViewportManager_SetRegionRect():
    pass


def ViewportManager_SetRegionRect2():
    pass


def ViewportManager_SetRotationIncrement():
    pass


def ViewportManager_SetViewportGridVisible():
    pass


def ViewportManager_SetViewportLayout():
    pass


def ViewportManager_SetViewportMax():
    pass


def ViewportManager_ViewportInvalidate():
    pass


def ViewportManager_ViewportInvalidateBkgImage():
    pass


def ViewportManager_ViewportZoomExtents():
    pass


def ViewportManager_ZoomToBounds():
    pass


def ViewportsBackground_GetColor():
    pass


def ViewportsBackground_GetColorController():
    pass


def ViewportsBackground_GetFrameNumber():
    pass


def ViewportsBackground_GetFrameRange():
    pass


def ViewportsBackground_GetImageAnimate():
    pass


def ViewportsBackground_GetImageAspect():
    pass


def ViewportsBackground_GetImageAsset():
    pass


def ViewportsBackground_GetOutOfRangeType():
    pass


def ViewportsBackground_GetStartTime():
    pass


def ViewportsBackground_GetSyncFrame():
    pass


def ViewportsBackground_SetColor():
    pass


def ViewportsBackground_SetColorController():
    pass


def ViewportsBackground_SetFrameRange():
    pass


def ViewportsBackground_SetImageAnimate():
    pass


def ViewportsBackground_SetImageAspect():
    pass


def ViewportsBackground_SetImageAsset():
    pass


def ViewportsBackground_SetOutOfRangeType():
    pass


def ViewportsBackground_SetStartTime():
    pass


def ViewportsBackground_SetSyncFrame():
    pass


def Win32_GetCheckBox():
    pass


def Win32_GetMAXHWnd():
    pass


def Win32_GetStatusPanelHWnd():
    pass


def Win32_GetViewPortHWnd():
    pass


def Win32_IsHovering():
    pass


def Win32_IsThemeSupported():
    pass


def Win32_IsVistaAeroEnabled():
    pass


def Win32_MakeButton2State():
    pass


def Win32_MakeButton3State():
    pass


def Win32_RegisterDialogWindow():
    pass


def Win32_RevealInExplorer():
    pass


def Win32_Set3dsMaxAsParentWindow():
    pass


def Win32_SetCheckBox():
    pass


def Win32_UnRegisterDialogWindow():
    pass


def WSModifier__CastFrom():
    pass


def WStr_MatchPattern():
    pass


def WStr_MaxAlphaNumCompare():
    pass


def WStr_MaxAlphaNumCompareNoCase():
    pass


def XRefs_GetIncludeInHierarchy():
    pass


def XRefs_IsAutoUpdateSuspended():
    pass


def XRefs_SceneSetIgnoreFlag():
    pass


def XRefs_SetAutoUpdateSuspended():
    pass


def XRefs_SetIncludeInHierarchy():
    pass


def XRefs_UpdateSceneXRefState():
    pass

#end of MaxPlus.py file