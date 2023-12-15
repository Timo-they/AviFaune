



import typing
from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QLabel, QSizePolicy, QApplication
from PyQt5.QtCore import QObject, QEvent, Qt

import datas

from top_layout.central_view_photo.cadre import Cadre


class CentralPhoto(QWidget):

    qlabel: QLabel

    cadres: list

    def __init__(self, parent = None):
        super().__init__(parent)
        datas.set_widget("central_photo", self)

        self.cadres = []
        self.cadre_mode = ""
        # Can be : "hover", "resize", "add", "edit_specie", "delete"

        # If currently resizing a cadre
        self.resizing = False

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setMinimumHeight(100)

        self.qlabel = QLabel(self)
        self.qlabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.qlabel.setScaledContents(True)

        self.qlabel.setMouseTracking(True)
        self.qlabel.installEventFilter(self)
        
        self.installEventFilter(self)
    
    # Quand la fenêtre est resize
    def eventFilter(self, object: QObject, event: QEvent) -> bool:
        event_lookup = {"0": "QEvent::None",
                "114": "QEvent::ActionAdded",
                "113": "QEvent::ActionChanged",
                "115": "QEvent::ActionRemoved",
                "99": "QEvent::ActivationChange",
                "121": "QEvent::ApplicationActivate",
                "122": "QEvent::ApplicationDeactivate",
                "36": "QEvent::ApplicationFontChange",
                "37": "QEvent::ApplicationLayoutDirectionChange",
                "38": "QEvent::ApplicationPaletteChange",
                "214": "QEvent::ApplicationStateChange",
                "35": "QEvent::ApplicationWindowIconChange",
                "68": "QEvent::ChildAdded",
                "69": "QEvent::ChildPolished",
                "71": "QEvent::ChildRemoved",
                "40": "QEvent::Clipboard",
                "19": "QEvent::Close",
                "200": "QEvent::CloseSoftwareInputPanel",
                "178": "QEvent::ContentsRectChange",
                "82": "QEvent::ContextMenu",
                "183": "QEvent::CursorChange",
                "52": "QEvent::DeferredDelete",
                "60": "QEvent::DragEnter",
                "62": "QEvent::DragLeave",
                "61": "QEvent::DragMove",
                "63": "QEvent::Drop",
                "170": "QEvent::DynamicPropertyChange",
                "98": "QEvent::EnabledChange",
                "10": "QEvent::Enter",
                "150": "QEvent::EnterEditFocus",
                "124": "QEvent::EnterWhatsThisMode",
                "206": "QEvent::Expose",
                "116": "QEvent::FileOpen",
                "8": "QEvent::FocusIn",
                "9": "QEvent::FocusOut",
                "23": "QEvent::FocusAboutToChange",
                "97": "QEvent::FontChange",
                "198": "QEvent::Gesture",
                "202": "QEvent::GestureOverride",
                "188": "QEvent::GrabKeyboard",
                "186": "QEvent::GrabMouse",
                "159": "QEvent::GraphicsSceneContextMenu",
                "164": "QEvent::GraphicsSceneDragEnter",
                "166": "QEvent::GraphicsSceneDragLeave",
                "165": "QEvent::GraphicsSceneDragMove",
                "167": "QEvent::GraphicsSceneDrop",
                "163": "QEvent::GraphicsSceneHelp",
                "160": "QEvent::GraphicsSceneHoverEnter",
                "162": "QEvent::GraphicsSceneHoverLeave",
                "161": "QEvent::GraphicsSceneHoverMove",
                "158": "QEvent::GraphicsSceneMouseDoubleClick",
                "155": "QEvent::GraphicsSceneMouseMove",
                "156": "QEvent::GraphicsSceneMousePress",
                "157": "QEvent::GraphicsSceneMouseRelease",
                "182": "QEvent::GraphicsSceneMove",
                "181": "QEvent::GraphicsSceneResize",
                "168": "QEvent::GraphicsSceneWheel",
                "18": "QEvent::Hide",
                "27": "QEvent::HideToParent",
                "127": "QEvent::HoverEnter",
                "128": "QEvent::HoverLeave",
                "129": "QEvent::HoverMove",
                "96": "QEvent::IconDrag",
                "101": "QEvent::IconTextChange",
                "83": "QEvent::InputMethod",
                "207": "QEvent::InputMethodQuery",
                "169": "QEvent::KeyboardLayoutChange",
                "6": "QEvent::KeyPress",
                "7": "QEvent::KeyRelease",
                "89": "QEvent::LanguageChange",
                "90": "QEvent::LayoutDirectionChange",
                "76": "QEvent::LayoutRequest",
                "11": "QEvent::Leave",
                "151": "QEvent::LeaveEditFocus",
                "125": "QEvent::LeaveWhatsThisMode",
                "88": "QEvent::LocaleChange",
                "176": "QEvent::NonClientAreaMouseButtonDblClick",
                "174": "QEvent::NonClientAreaMouseButtonPress",
                "175": "QEvent::NonClientAreaMouseButtonRelease",
                "173": "QEvent::NonClientAreaMouseMove",
                "177": "QEvent::MacSizeChange",
                "43": "QEvent::MetaCall",
                "102": "QEvent::ModifiedChange",
                "4": "QEvent::MouseButtonDblClick",
                "2": "QEvent::MouseButtonPress",
                "3": "QEvent::MouseButtonRelease",
                "5": "QEvent::MouseMove",
                "109": "QEvent::MouseTrackingChange",
                "13": "QEvent::Move",
                "197": "QEvent::NativeGesture",
                "208": "QEvent::OrientationChange",
                "12": "QEvent::Paint",
                "39": "QEvent::PaletteChange",
                "131": "QEvent::ParentAboutToChange",
                "21": "QEvent::ParentChange",
                "212": "QEvent::PlatformPanel",
                "217": "QEvent::PlatformSurface",
                "75": "QEvent::Polish",
                "74": "QEvent::PolishRequest",
                "123": "QEvent::QueryWhatsThis",
                "106": "QEvent::ReadOnlyChange",
                "199": "QEvent::RequestSoftwareInputPanel",
                "14": "QEvent::Resize",
                "204": "QEvent::ScrollPrepare",
                "205": "QEvent::Scroll",
                "117": "QEvent::Shortcut",
                "51": "QEvent::ShortcutOverride",
                "17": "QEvent::Show",
                "26": "QEvent::ShowToParent",
                "50": "QEvent::SockAct",
                "192": "QEvent::StateMachineSignal",
                "193": "QEvent::StateMachineWrapped",
                "112": "QEvent::StatusTip",
                "100": "QEvent::StyleChange",
                "87": "QEvent::TabletMove",
                "92": "QEvent::TabletPress",
                "93": "QEvent::TabletRelease",
                "171": "QEvent::TabletEnterProximity",
                "172": "QEvent::TabletLeaveProximity",
                "219": "QEvent::TabletTrackingChange",
                "22": "QEvent::ThreadChange",
                "1": "QEvent::Timer",
                "120": "QEvent::ToolBarChange",
                "110": "QEvent::ToolTip",
                "184": "QEvent::ToolTipChange",
                "194": "QEvent::TouchBegin",
                "209": "QEvent::TouchCancel",
                "196": "QEvent::TouchEnd",
                "195": "QEvent::TouchUpdate",
                "189": "QEvent::UngrabKeyboard",
                "187": "QEvent::UngrabMouse",
                "78": "QEvent::UpdateLater",
                "77": "QEvent::UpdateRequest",
                "111": "QEvent::WhatsThis",
                "118": "QEvent::WhatsThisClicked",
                "31": "QEvent::Wheel",
                "132": "QEvent::WinEventAct",
                "24": "QEvent::WindowActivate",
                "103": "QEvent::WindowBlocked",
                "25": "QEvent::WindowDeactivate",
                "34": "QEvent::WindowIconChange",
                "105": "QEvent::WindowStateChange",
                "33": "QEvent::WindowTitleChange",
                "104": "QEvent::WindowUnblocked",
                "203": "QEvent::WinIdChange",
                "126": "QEvent::ZOrderChange", }
        # print(event_lookup[str(event.type())], object)

        if object == self and event.type() == QEvent.Resize and not self.qlabel.pixmap() == None:
            self.resize()

        elif object == self.qlabel and event.type() == QEvent.MouseMove and not self.resizing:
            QApplication.setOverrideCursor(Qt.CrossCursor)
        
        elif object == self.qlabel and event.type() == QEvent.MouseMove and self.resizing:
            x = event.x()
            y = event.y()
            print(x, y, self.resizing.end_x)
            # cadre_x = int((x - w/2) * qlabel_width / pixmap_width)
            # cadre_y = int((y - h/2) * qlabel_height / pixmap_height)
            # cadre_width = int(w * qlabel_width / pixmap_width)
            # cadre_height = int(h * qlabel_height / pixmap_height)
            # self.resizing.x = int(x  * self.qlabel.pixmap().width() / self.qlabel.width() + self.resizing.w/2)
            # self.resizing.y = int(y  * self.qlabel.pixmap().height() / self.qlabel.height() + self.resizing.h/2)
            # self.resizing.w = (self.resizing.end_x - self.resizing.x) 
            # self.resizing.h += (last_y - self.resizing.y) * self.qlabel.pixmap().height() / self.qlabel.height()
            # self.resizing.resize()

            match self.resizing.resizing_anchor:
                case "left_top":
                    QApplication.setOverrideCursor(Qt.SizeFDiagCursor)
                case "left_bot":
                    QApplication.setOverrideCursor(Qt.SizeBDiagCursor)
                case "left_mid":
                    QApplication.setOverrideCursor(Qt.SizeHorCursor)
                case "right_top":
                    QApplication.setOverrideCursor(Qt.SizeBDiagCursor)
                case "right_bot":
                    QApplication.setOverrideCursor(Qt.SizeFDiagCursor)
                case "right_mid":
                    QApplication.setOverrideCursor(Qt.SizeHorCursor)
                case "mid_top":
                    QApplication.setOverrideCursor(Qt.SizeVerCursor)
                case "mid_bot":
                    QApplication.setOverrideCursor(Qt.SizeVerCursor)
                case "mid":
                    QApplication.setOverrideCursor(Qt.SizeAllCursor)

        return super().eventFilter(object, event)

    # On centre l'image sur le QWidget
    def resize(self):
        widget_ratio = self.width() / self.height()
        qlabel_ratio = self.qlabel.pixmap().width() / self.qlabel.pixmap().height()

        if widget_ratio >= qlabel_ratio:
            # Widget trop large
            qlabel_x = int(self.width() / 2 - self.height() * qlabel_ratio / 2)
            qlabel_y = 0
            qlabel_width = int(self.height() * qlabel_ratio)
            qlabel_height = int(self.height())

            self.qlabel.setGeometry(qlabel_x, qlabel_y, qlabel_width, qlabel_height)
        
        else:
            # Widget trop haut
            qlabel_x = 0
            qlabel_y = int(self.height() / 2 - self.width() / qlabel_ratio / 2)
            qlabel_width = int(self.width())
            qlabel_height = int(self.width() / qlabel_ratio)

            self.qlabel.setGeometry(qlabel_x, qlabel_y, qlabel_width, qlabel_height)
        
        for cadre in self.cadres:
            cadre.resize()

    
    def set_pixmap(self, photo_pixmap):
        #self.initial_pixmap = photo_pixmap
        self.qlabel.setPixmap(photo_pixmap)
        self.resize()
        self.remove_cadres()
    
    def remove_cadres(self):
        for cadre in self.cadres:
            cadre.deleteLater()
        
        self.cadres = []
    
    def update_boxes(self):
        self.remove_cadres()

        if datas.get_current_photo() == "":
            print("Updating central photo boxes, to None")
            return
        
        boxes = datas.get_boxes_current_photo()
        print("Updating central photo boxes, to ", boxes)

        for id, data in boxes.items():
            specie, x, y, w, h, prob = data["specie"], data["x"], data["y"], data["w"], data["h"], data["prob"]

            print("Showing box ", specie, x, y, w, h, prob)

            cadre = Cadre(specie, x, y, w, h, prob, self.qlabel, self.qlabel.pixmap())
            cadre.show()
            self.cadres.append(cadre)


    # def set_boxes(self, boxes_classes, boxes_shapes):
    #     # On enlève tous les cadres de la photo
    #     self.remove_cadres()
        
    #     for i in range(len(boxes_shapes)):
    #         cadre = Cadre(boxes_classes[i], boxes_shapes[i], self.qlabel, self.qlabel.pixmap())
    #         cadre.show()
    #         self.cadres.append(cadre)

