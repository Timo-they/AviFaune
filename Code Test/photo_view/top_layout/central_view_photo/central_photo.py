



import typing
from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QLabel, QSizePolicy, QApplication, QPushButton, QComboBox
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
        self.cadre_mode = "normal"
        # Can be : "normal", "resize", "add", "delete"
        self.offset = None

        # If currently resizing a cadre
        self.resizing = False

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setMinimumHeight(100)

        self.qlabel = QLabel(self)
        self.qlabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.qlabel.setScaledContents(True)

        self.qlabel.setMouseTracking(True)
        self.qlabel.installEventFilter(self)
        
        offset = 5
        self.toolbutton_none = QPushButton("Survoler", self)
        self.toolbutton_none.installEventFilter(self)
        self.toolbutton_none.move(offset, offset)
        self.toolbutton_none.pressed.connect(self.normal_mode)
        self.toolbutton_none.setDisabled(True)

        self.toolbutton_resize = QPushButton("Redimmensionner", self)
        self.toolbutton_resize.installEventFilter(self)
        self.toolbutton_resize.move(offset*2 + self.toolbutton_none.width(), offset)
        self.toolbutton_resize.pressed.connect(self.resize_mode)

        self.toolbutton_add = QPushButton("Ajouter", self)
        self.toolbutton_add.installEventFilter(self)
        self.toolbutton_add.move(self.toolbutton_resize.x() + offset + self.toolbutton_resize.width(), offset)
        self.toolbutton_add.pressed.connect(self.add_mode)

        self.comboBox = QComboBox(self)
        for specie in datas.get_species().values():
            self.comboBox.addItem(specie)

        # Connectez la méthode de gestion d'événements lorsque la sélection change
        #self.comboBox.currentIndexChanged.connect(self.on_selection_changed)
        self.comboBox.move(self.toolbutton_add.x() + offset + self.toolbutton_add.width(), offset)
        self.comboBox.setFixedHeight(self.toolbutton_add.height())
        self.comboBox.setVisible(False)
        
        self.setFocusPolicy(Qt.ClickFocus)
        self.installEventFilter(self)
    
    def normal_mode(self):
        self.toolbutton_none.setDisabled(True)
        self.toolbutton_resize.setDisabled(False)
        self.toolbutton_add.setDisabled(False)
        self.cadre_mode = "normal"
        self.resizing = None
        self.comboBox.setVisible(False)
    
    def resize_mode(self):
        self.toolbutton_none.setDisabled(False)
        self.toolbutton_resize.setDisabled(True)
        self.toolbutton_add.setDisabled(False)
        self.cadre_mode = "resize"
        self.resizing = None
        self.comboBox.setVisible(False)
    
    def add_mode(self):
        self.toolbutton_none.setDisabled(False)
        self.toolbutton_resize.setDisabled(False)
        self.toolbutton_add.setDisabled(True)
        self.cadre_mode = "add"
        self.resizing = None
        self.comboBox.setVisible(True)

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
        # print(event_lookup[str(event.type())])
        min_cadre_size = 30

        if (object == self.toolbutton_none or object == self.toolbutton_resize or object == self.toolbutton_add) and event.type() == QEvent.Resize:
            offset = 10
            self.toolbutton_none.move(offset, offset)
            self.toolbutton_resize.move(offset*2 + self.toolbutton_none.width(), offset)
            self.toolbutton_add.move(self.toolbutton_resize.x() + offset + self.toolbutton_resize.width(), offset)
            self.comboBox.move(self.toolbutton_add.x() + offset + self.toolbutton_add.width(), offset)
        
        elif object == self and event.type() == QEvent.Resize and not self.qlabel.pixmap() == None:
            self.resize()

        elif object == self.qlabel and (event.type() == QEvent.MouseMove or event.type() == QEvent.Enter) and self.cadre_mode == "add" and not self.resizing:
            QApplication.setOverrideCursor(Qt.CrossCursor)
        
        elif object == self.qlabel and event.type() == QEvent.Leave and self.cadre_mode == "add":
            QApplication.restoreOverrideCursor()

            if self.resizing:
                self.resizing == None
        
        elif object == self.qlabel and event.type() == QEvent.MouseMove and self.resizing and (self.cadre_mode == "resize" or self.cadre_mode == "add"):
            mouse_screen_x = event.x()
            mouse_screen_y = event.y()

            # print(mouse_screen_x, mouse_screen_y, self.resizing.end_x_photo)

            match self.resizing.resizing_anchor:
                case "left_top":
                    QApplication.setOverrideCursor(Qt.SizeFDiagCursor)
                    self.resizing.x_photo = int(self.screen_to_photo(mouse_screen_x))
                    self.resizing.w = int(self.resizing.end_x_photo - self.resizing.x_photo)
                    self.resizing.y_photo = int(self.screen_to_photo(mouse_screen_y))
                    self.resizing.h = int(self.resizing.end_y_photo - self.resizing.y_photo)

                case "left_bot":
                    QApplication.setOverrideCursor(Qt.SizeBDiagCursor)
                    self.resizing.x_photo = int(self.screen_to_photo(mouse_screen_x))
                    self.resizing.w = int(self.resizing.end_x_photo - self.resizing.x_photo)
                    self.resizing.h = int(self.screen_to_photo(mouse_screen_y) - self.resizing.y_photo)

                case "left_mid":
                    QApplication.setOverrideCursor(Qt.SizeHorCursor)
                    self.resizing.x_photo = int(self.screen_to_photo(mouse_screen_x))
                    self.resizing.w = int(self.resizing.end_x_photo - self.resizing.x_photo)

                case "right_top":
                    QApplication.setOverrideCursor(Qt.SizeBDiagCursor)
                    self.resizing.w = int(self.screen_to_photo(mouse_screen_x) - self.resizing.x_photo)
                    self.resizing.y_photo = int(self.screen_to_photo(mouse_screen_y))
                    self.resizing.h = int(self.resizing.end_y_photo - self.resizing.y_photo)

                case "right_bot":
                    QApplication.setOverrideCursor(Qt.SizeFDiagCursor)
                    self.resizing.w = int(self.screen_to_photo(mouse_screen_x) - self.resizing.x_photo)
                    self.resizing.h = int(self.screen_to_photo(mouse_screen_y) - self.resizing.y_photo)

                case "right_mid":
                    QApplication.setOverrideCursor(Qt.SizeHorCursor)
                    self.resizing.w = int(self.screen_to_photo(mouse_screen_x) - self.resizing.x_photo)

                case "mid_top":
                    QApplication.setOverrideCursor(Qt.SizeVerCursor)
                    self.resizing.y_photo = int(self.screen_to_photo(mouse_screen_y))
                    self.resizing.h = int(self.resizing.end_y_photo - self.resizing.y_photo)

                case "mid_bot":
                    QApplication.setOverrideCursor(Qt.SizeVerCursor)
                    self.resizing.h = int(self.screen_to_photo(mouse_screen_y) - self.resizing.y_photo)

                case "mid":
                    QApplication.setOverrideCursor(Qt.SizeAllCursor)
                    if self.offset == None:
                        self.offset = (self.photo_to_screen(self.resizing.x_photo) - mouse_screen_x, self.photo_to_screen(self.resizing.y_photo) - mouse_screen_y)
                    
                    else:
                        self.resizing.x_photo = int(self.screen_to_photo(mouse_screen_x + self.offset[0]))
                        self.resizing.y_photo = int(self.screen_to_photo(mouse_screen_y + self.offset[1]))
            
            if self.resizing.resizing_anchor == "mid":
                if self.resizing.x_photo < 0:
                    self.resizing.x_photo = 0
                elif self.resizing.x_photo > self.qlabel.pixmap().width() - self.resizing.w:
                    self.resizing.x_photo = int(self.qlabel.pixmap().width() - self.resizing.w)
                
                if self.resizing.y_photo < 0:
                    self.resizing.y_photo = 0
                elif self.resizing.y_photo > self.qlabel.pixmap().height() - self.resizing.h:
                    self.resizing.y_photo = int(self.qlabel.pixmap().height() - self.resizing.h)
                

            else:
                if self.resizing.x_photo < 0:
                    self.resizing.x_photo = 0
                elif self.resizing.x_photo > self.qlabel.pixmap().width() - min_cadre_size:
                    self.resizing.x_photo = int(self.qlabel.pixmap().width() - min_cadre_size)
                
                if self.resizing.y_photo < 0:
                    self.resizing.y_photo = 0
                elif self.resizing.y_photo > self.qlabel.pixmap().height() - min_cadre_size:
                    self.resizing.y_photo = int(self.qlabel.pixmap().height() - min_cadre_size)
                
                if self.resizing.w < min_cadre_size:
                    self.resizing.w = min_cadre_size
                elif self.resizing.w > self.qlabel.pixmap().width() - self.resizing.x_photo:
                    self.resizing.w = self.qlabel.pixmap().width() - self.resizing.x_photo
                
                if self.resizing.h < min_cadre_size:
                    self.resizing.h = min_cadre_size
                elif self.resizing.h > self.qlabel.pixmap().height() - self.resizing.y_photo:
                    self.resizing.h = self.qlabel.pixmap().height() - self.resizing.y_photo
            
            datas.update_pos_box_photo(
                self.resizing.id_box,
                self.resizing.x_photo,
                self.resizing.y_photo,
                self.resizing.w,
                self.resizing.h
            )

            self.resizing.resize()
        
        elif object == self.qlabel and event.type() == QEvent.MouseButtonPress:
            if event.button() == Qt.LeftButton and self.cadre_mode == "add" and not self.resizing:
                print("Clicked to initialize add cadre", event.x(), event.y())

                x = str(int(self.screen_to_photo(event.x())))
                y = str(int(self.screen_to_photo(event.y())))
                w = str(min_cadre_size)
                h = str(min_cadre_size)
                ok_specie = [i for i in datas.get_species() if datas.get_species()[i] == self.comboBox.currentText()]
                specie = "-1" if ok_specie == [] else ok_specie[0]

                print(w, y, w, h, specie)

                id_box = datas.add_box_photo(datas.get_current_photo(), specie, x, y, w, h, "1.0")

                for cadre in self.cadres:
                    if cadre.id_box == id_box:
                        self.resizing = cadre
                        cadre.resizing_anchor = "right_bot"
                        cadre.end_x_photo = self.screen_to_photo(event.x()) + min_cadre_size
                        cadre.end_y_photo = self.screen_to_photo(event.y()) + min_cadre_size
                
                QApplication.setOverrideCursor(Qt.SizeFDiagCursor)
        
        elif event.type() == QEvent.MouseButtonRelease:
            if event.button() == Qt.LeftButton and self.cadre_mode == "add":
                self.resizing = None
                QApplication.restoreOverrideCursor()
                
                print("Released the newly added cadre")

        return super().eventFilter(object, event)

    def photo_to_screen(self, coord_photo: int):
        return coord_photo * self.qlabel.width() / self.qlabel.pixmap().width()
    
    def screen_to_photo(self, coord_screen: int):
        return coord_screen * self.qlabel.pixmap().width() / self.qlabel.width()

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
        self.resizing = None
    
    def remove_cadres(self):
        for cadre in self.cadres:
            cadre.deleteLater()
        
        self.cadres = []
    
    def update_boxes(self):
        self.resizing = None
        self.remove_cadres()

        if datas.get_current_photo() == "":
            print("Updating central photo boxes, to None")
            return
        
        boxes = datas.get_boxes_current_photo()
        print("Updating central photo boxes, to ", boxes)

        for id, data in boxes.items():
            specie, x, y, w, h, prob = data["specie"], data["x"], data["y"], data["w"], data["h"], data["prob"]

            print("Showing box ", specie, x, y, w, h, prob)

            cadre = Cadre(id, specie, x, y, w, h, prob, self.qlabel, self.qlabel.pixmap())
            cadre.show()
            self.cadres.append(cadre)
    
    def update_species(self):
        self.comboBox.clear()
        for specie in datas.get_species().values():
            self.comboBox.addItem(specie)

