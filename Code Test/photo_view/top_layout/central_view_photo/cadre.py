


from functools import partial

from PyQt5 import QtGui
from PyQt5.QtCore import QEvent, QObject, Qt
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QMenu, QAction
from PyQt5.QtGui import QCursor

import datas


class Cadre(QLabel):

    def __init__(self, id_box, specie, x, y, w, h, prob, qlabel, pixmap):
        super().__init__(qlabel)

        self.resizing_anchor = ""

        self.id_box = id_box
        self.specie = str(int(specie))
        self.x_photo, self.y_photo, self.w, self.h = int(x), int(y), int(w), int(h)
        #self.x_photo, self.y_photo = int(self.x_photo - self.w/2), int(self.y_photo - self.h/2)

        self.qlabel = qlabel
        self.pixmap = pixmap

        self.label = QLabel(datas.get_specie_name(specie) + " " + prob, self)
        self.label.setObjectName("cadre_label")

        # TODO : Set cadre color depending on specie
        print("TODO : Set cadre color depending on specie")

        self.setStyleSheet("#cadre {border: 2px solid #" + datas.get_color_specie(self.specie) + ";} #cadre:hover { background: #22" + datas.get_color_specie(self.specie) + ";} #cadre_label {padding: 2px;background-color: #aa" + datas.get_color_specie(self.specie) + ";}")

        self.setObjectName("cadre")
        self.setToolTip(datas.get_specie_name(specie) + " " + prob)
        self.resize()

        self.setMouseTracking(True)
        self.installEventFilter(self)
    
    def resize(self):
        x, y, w, h = self.x_photo, self.y_photo, self.w, self.h

        # print("Box : ", x, y, w, h)

        qlabel_x = self.qlabel.x()
        qlabel_y = self.qlabel.y()
        qlabel_width = self.qlabel.width()
        qlabel_height = self.qlabel.height()
        # print("QLabel : ", qlabel_x, qlabel_y ,qlabel_width, qlabel_height)

        pixmap_width = self.pixmap.width()
        pixmap_height = self.pixmap.height()
        # print("QPixmap : ", pixmap_width, pixmap_height)

        cadre_x = int(x * qlabel_width / pixmap_width)
        cadre_y = int(y * qlabel_height / pixmap_height)
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
        
        handle_zone_size = 5

        if (event.type() == QEvent.HoverMove or event.type() == QEvent.HoverEnter) and not datas.get_widget("central_photo").resizing and datas.get_widget("central_photo").cadre_mode == "resize":
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
        
        if event.type() == QEvent.HoverLeave and not datas.get_widget("central_photo").resizing and datas.get_widget("central_photo").cadre_mode == "resize":
            QApplication.restoreOverrideCursor()

        elif event.type() == QEvent.MouseButtonPress:
            if event.button() == Qt.LeftButton and datas.get_widget("central_photo").cadre_mode == "resize":
                self.end_x_photo = self.x_photo + self.w
                self.end_y_photo = self.y_photo + self.h
                datas.get_widget("central_photo").resizing = self
            
            elif event.button() == Qt.RightButton and (datas.get_widget("central_photo").cadre_mode == "normal" or datas.get_widget("central_photo").cadre_mode == "resize"):
                menu = QMenu(self)

                for id, specie in datas.get_species().items():
                    change_specie_action = QAction(specie, self)
                    change_specie_action.triggered.connect(partial(self.change_specie_box, self.id_box, id))
                    menu.addAction(change_specie_action)

                menu.addSeparator()

                delete_oizo_action = QAction("Supprimer l'oiseau", self)
                delete_oizo_action.triggered.connect(partial(self.delete_oizo_box, self.id_box))
                menu.addAction(delete_oizo_action)

                menu.popup(QCursor.pos())
        
        elif event.type() == QEvent.MouseButtonRelease and datas.get_widget("central_photo").cadre_mode == "resize":
            if event.button() == Qt.LeftButton:
                QApplication.restoreOverrideCursor()
                datas.get_widget("central_photo").resizing = None
                datas.get_widget("central_photo").offset = None

        return super().eventFilter(object, event)
    
    def change_specie_box(self, id_box, id_specie):
        datas.update_specie_box_photo(id_box, id_specie)
    
    def delete_oizo_box(self, id_box):
        datas.delete_box_photo(id_box)