


import typing
from PyQt5 import QtGui
from PyQt5.QtCore import QEvent, QObject, Qt
from PyQt5.QtWidgets import QWidget, QLabel, QApplication

import datas


class Cadre(QLabel):

    def __init__(self, specie, x, y, w, h, prob, qlabel, pixmap):
        super().__init__(qlabel)

        self.last_x = 0
        self.last_y = 0
        self.resizing_anchor = ""

        self.specie = str(int(specie))
        self.x, self.y, self.w, self.h = x, y, w, h
        self.x, self.y, self.w, self.h = int(self.x), int(self.y), int(self.w), int(self.h)

        self.qlabel = qlabel
        self.pixmap = pixmap

        self.label = QLabel(datas.get_specie_name(specie) + " " + prob, self)
        self.label.setObjectName("cadre_label")

        # self.label = QLabel(self)
        # self.label.setText("5")
        # self.label.move(10, 10)

        # TODO : Set cadre color depending on specie
        print("TODO : Set cadre color depending on specie")

        self.setObjectName("cadre")
        self.setToolTip(datas.get_specie_name(specie) + " " + prob)
        self.resize()

        self.setMouseTracking(True)
        self.installEventFilter(self)
    
    def resize(self):
        x, y, w, h = self.x, self.y, self.w, self.h
        x, y, w, h = int(x), int(y), int(w), int(h)

        # print("Box : ", x, y, w, h)

        qlabel_x = self.qlabel.x()
        qlabel_y = self.qlabel.y()
        qlabel_width = self.qlabel.width()
        qlabel_height = self.qlabel.height()
        # print("QLabel : ", qlabel_x, qlabel_y ,qlabel_width, qlabel_height)

        pixmap_width = self.pixmap.width()
        pixmap_height = self.pixmap.height()
        # print("QPixmap : ", pixmap_width, pixmap_height)

        cadre_x = int((x - w/2) * qlabel_width / pixmap_width)
        cadre_y = int((y - h/2) * qlabel_height / pixmap_height)
        cadre_width = int(w * qlabel_width / pixmap_width)
        cadre_height = int(h * qlabel_height / pixmap_height)
        
        self.setGeometry(cadre_x, cadre_y, cadre_width, cadre_height)
        # print("Added cadre at ", cadre_x, cadre_y, cadre_width, cadre_height)

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
        # print(event_lookup[str(event.type())])
        
        handle_zone_size = 10
        qlabel_width = self.qlabel.width()
        qlabel_height = self.qlabel.height()
        # print("QLabel : ", qlabel_x, qlabel_y ,qlabel_width, qlabel_height)

        pixmap_width = self.pixmap.width()
        pixmap_height = self.pixmap.height()
        # print("QPixmap : ", pixmap_width, pixmap_height)

        if event.type() == QEvent.HoverMove and not datas.get_widget("central_photo").resizing:
            #print(event.pos())
            x = event.pos().x()
            y = event.pos().y()

            # Left
            if x < handle_zone_size:
                # Top
                if y < handle_zone_size:
                    QApplication.setOverrideCursor(Qt.SizeFDiagCursor)
                    self.resizing_anchor = "left_top"

                # Bot
                elif y > self.height() - handle_zone_size:
                    QApplication.setOverrideCursor(Qt.SizeBDiagCursor)
                    self.resizing_anchor = "left_bot"

                # Mid
                else:
                    QApplication.setOverrideCursor(Qt.SizeHorCursor)
                    self.resizing_anchor = "left_mid"
            
            # Right
            elif x > self.width() - handle_zone_size:
                # Top
                if y < handle_zone_size:
                    QApplication.setOverrideCursor(Qt.SizeBDiagCursor)
                    self.resizing_anchor = "right_top"

                # Bot
                elif y > self.height() - handle_zone_size:
                    QApplication.setOverrideCursor(Qt.SizeFDiagCursor)
                    self.resizing_anchor = "right_bot"

                # Mid
                else:
                    QApplication.setOverrideCursor(Qt.SizeHorCursor)
                    self.resizing_anchor = "right_mid"

            # Mid
            else:
                # Top
                if y < handle_zone_size:
                    QApplication.setOverrideCursor(Qt.SizeVerCursor)
                    self.resizing_anchor = "mid_top"

                # Bot
                elif y > self.height() - handle_zone_size:
                    QApplication.setOverrideCursor(Qt.SizeVerCursor)
                    self.resizing_anchor = "mid_bot"
                
                else:
                    #QApplication.setOverrideCursor(Qt.ArrowCursor)
                    QApplication.setOverrideCursor(Qt.SizeAllCursor)
                    self.resizing_anchor = "mid"

            return False

        elif event.type() == QEvent.MouseButtonPress:
            datas.get_widget("central_photo").resizing = self
            self.end_x = self.x + self.w
            self.end_y = self.y + self.h
        
        elif event.type() == QEvent.MouseButtonRelease:
            datas.get_widget("central_photo").resizing = None

        # elif event.type() == QEvent.MouseMove and datas.get_widget("central_photo").resizing:
        #     x = event.x()
        #     y = event.y()

        #     print(x, y, self.resizing_anchor)

        #     match self.resizing_anchor:
        #         case "left_top":
        #             self.x = self.initial_x + x * pixmap_width / qlabel_width
        #             self.y = self.initial_y + y * pixmap_height / qlabel_height
        #             # self.x += (x - self.last_x) * qlabel_width / pixmap_width
        #             # self.y += (y - self.last_y) * qlabel_height / pixmap_height
        #             # self.w += - (x - self.last_x)  * qlabel_width / pixmap_width
        #             # self.h += - (y - self.last_y) * qlabel_height / pixmap_height
        #             self.resize()

        #         case "left_bot":
        #             pass

        #         case "left_mid":
        #             pass
            
        #         case "right_top":
        #             pass

        #         case "right_bot":
        #             pass

        #         case "right_mid":
        #             pass

        #         case "mid_top":
        #             pass

        #         case "mid_bot":
        #             pass
                
        #         case "":
        #             pass
            

        return super().eventFilter(object, event)
