from PySide6.QtWidgets import QMainWindow, QDialog, QFileDialog,QTextEdit

from UI.Main_window_ui import Ui_MainWindow  # Main_window.py
from UI.btn_DataFlip_ui import Ui_Dialog_DataFlip as Ui_DataFlip # Data Flip Dialog
from UI.btn_FileRename_ui import Ui_Dialog_FileRename as Ui_FileRename # Data File Rename Dialog
from UI.btn_ImageView_ui import Ui_MainWindow_ImageView as Ui_ViewImage # Bounding Box Drawing MainWindow
from UI.btn_PloygonDraw_ui import Ui_Dialog_PolygonDraw as Ui_PolygonDraw # Ploygon Drawing Dialog
from UI.btn_DataAnalysis_ui import Ui_Dialog_DataAnalysis as Ui_DataAnalysis # Ploygon Drawing Dialog
from UI.btn_DatasetCheck_ui import Ui_Dialog_DatasetCheck as Ui_DatasetCheck # Ploygon Drawing Dialog


from UI.madeBy_ui import Ui_Dialog as Ui_madeBy  

from PySide6.QtWidgets import QMainWindow, QDialog, QMessageBox, QTableWidgetItem, QAbstractScrollArea,QHeaderView
from PySide6.QtCore import Qt
from PySide6.QtGui import  QPixmap

import os
import re
from PIL import Image  # Pillow 라이브러리 사용
from natsort import natsorted #자연스러운 정렬하기 위한 라이브러리
from pathlib import Path #드래그앤드롭으로 경로 가져올때 사용하는 라이브러리


class MainController:
    def __init__(self):
        # 메인 창 초기화
        self.main_window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_window)

        # 메뉴바 액션 연결
        self.ui.actionmade_by.triggered.connect(self.open_madeBy)

        # 버튼 클릭 이벤트 연결
        self.ui.btn_DataFlip.clicked.connect(self.open_btn_DataFlip_window)
        self.ui.btn_FileRename.clicked.connect(self.open_btn_FileRename_window)
        self.ui.btn_ImageView.clicked.connect(self.open_btn_ImageView_window)
        self.ui.btn_PolygonDraw.clicked.connect(self.open_btn_PloygonDraw_window)
        self.ui.btn_DataAnalysis.clicked.connect(self.open_btn_DataAnalysis_window)
        self.ui.btn_DataCheck.clicked.connect(self.open_btn_DataCheck_window)
        #라디오 버튼 선택 상태 저장
        self.rename_selected_option = 'AllRename'  
        self.ImageView_selected_option_view = 'dual'  
        self.ImageView_selected_option_onoff = 'off'  

        #bboxDraw 메인윈도우 살려두기
        self.ImageView_window = None

    def run(self):
        # 메인 창 실행
        self.main_window.show()

    def drop_event_textEdit_generic(self, event, text_edit):
        urls = event.mimeData().urls()
        if urls:
            folder_path = urls[0].toLocalFile()
            text_edit.setPlainText(folder_path)
    def drag_enter_event(self, event):
        """QTextEdit 또는 기타 위젯이 드롭 허용 가능하도록 하는 함수"""
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
##----------------------------Dialog Open----------------------------#
    def open_madeBy(self):
        dialog = QDialog()
        ui = Ui_madeBy()
        ui.setupUi(dialog)
        dialog.exec()

    def open_btn_DataFlip_window(self):
        # 다이얼로그 생성 및 설정
        dialog = QDialog()
        ui = Ui_DataFlip()
        ui.setupUi(dialog)
        # 버튼 클릭 이벤트 연결
        ui.output_fileOpen.clicked.connect(lambda: self.browse_folder(ui.output_textEdit))
        ui.image_fileOpen.clicked.connect(lambda: self.browse_folder(ui.image_textEdit))
        ui.gt_fileOpen.clicked.connect(lambda: self.browse_folder(ui.gt_textEdit))
        ui.btn_run.clicked.connect(lambda: self.Data_flip(ui))

        #드래그 이벤트 처리
        ui.image_textEdit.dragEnterEvent = self.drag_enter_event
        ui.gt_textEdit.dragEnterEvent = self.drag_enter_event
        ui.output_textEdit.dragEnterEvent = self.drag_enter_event

        # dropEvent: lambda로 "어떤 QTextEdit에 적용할지" 넘김
        ui.image_textEdit.dropEvent = lambda e: self.drop_event_textEdit_generic(e, ui.image_textEdit)
        ui.gt_textEdit.dropEvent = lambda e: self.drop_event_textEdit_generic(e, ui.gt_textEdit)
        ui.output_textEdit.dropEvent = lambda e: self.drop_event_textEdit_generic(e, ui.output_textEdit)

        dialog.exec()

    def open_btn_FileRename_window(self):
        dialog = QDialog()
        ui = Ui_FileRename()
        ui.setupUi(dialog)
        #버튼 클릭 이벤트 연결
        ui.pbtn_input_path1.clicked.connect(lambda: self.browse_folder(ui.textEdit_input_path1))
        ui.pbtn_input_path2.clicked.connect(lambda: self.browse_folder(ui.textEdit_input_path2))
        ui.pbtn_run.clicked.connect(lambda: self.Data_Rename(ui))

        #드래그 이벤트 처리
        ui.textEdit_input_path1.dragEnterEvent = self.drag_enter_event
        ui.textEdit_input_path2.dragEnterEvent = self.drag_enter_event

        # dropEvent: lambda로 "어떤 QTextEdit에 적용할지" 넘김
        ui.textEdit_input_path1.dropEvent = lambda e: self.drop_event_textEdit_generic(e, ui.textEdit_input_path1)
        ui.textEdit_input_path2.dropEvent = lambda e: self.drop_event_textEdit_generic(e, ui.textEdit_input_path2)

        #라디오 버튼 클릭 이벤트 연결
        ui.rBtn_AllRename.toggled.connect(lambda checked: self.Rename_on_radio_button_toggled(checked, "AllRename",ui))
        ui.rBtn_PartRename.toggled.connect(lambda checked: self.Rename_on_radio_button_toggled(checked, "PartRename",ui))
        ui.rBtn_front.toggled.connect(lambda checked: self.Rename_on_radio_button_toggled(checked, "front",ui))
        ui.rBtn_rear.toggled.connect(lambda checked: self.Rename_on_radio_button_toggled(checked, "rear",ui))

        
        #TextEdit 비활성화
        ui.textEdit_OldString.setEnabled(False)

        ui.progressBar.setValue(0)

        dialog.exec()
    
    def open_btn_ImageView_window(self):
        # 창 객체를 멤버 변수에 저장해서 참조 유지
        self.ImageView_window = QMainWindow()
        self.ui_ImageView = Ui_ViewImage()
        self.ui_ImageView.setupUi(self.ImageView_window)
        self.ImageView_window.show()
        
        # path value
        self.first_gt_path = None
        self.first_image_path = None
        self.second_gt_path = None
        self.second_image_path = None
        self.ouput_path = None

        # 이미지 이동시킬 변수
        self.first_current_index = 0
        self.second_current_index = 0
        
        # 1st Path 하위 액션 연결
        self.ui_ImageView.action1st_GT.triggered.connect(lambda: self.open_folder("first", "GT"))
        self.ui_ImageView.action1st_Image_2.triggered.connect(lambda: self.open_folder("first", "Image"))
        # 2nd Path 하위 액션 연결
        self.ui_ImageView.action2nd_GT.triggered.connect(lambda: self.open_folder("second", "GT"))
        self.ui_ImageView.action2nd_Image_2.triggered.connect(lambda: self.open_folder("second", "Image"))
        #output path 액션 연결
        self.ui_ImageView.actionOutput_Path.triggered.connect(lambda: self.open_folder("output", "output"))

    
        #Viewing Select Radio Btn
        self.ui_ImageView.rBtn_1stPath.toggled.connect(lambda checked: self.view_on_radio_button_toggled(checked, "first"))
        self.ui_ImageView.rBtn_2ndPath.toggled.connect(lambda checked: self.view_on_radio_button_toggled(checked, "second"))
        self.ui_ImageView.rBtn_Dual.toggled.connect(lambda checked: self.view_on_radio_button_toggled(checked, "dual"))
        #Bounding Box On/Off Radio Btn
        self.ui_ImageView.rBtn_BboxOff.toggled.connect(lambda checked: self.box_on_radio_button_toggled(checked, "off"))
        self.ui_ImageView.rBtn_BboxOn.toggled.connect(lambda checked: self.box_on_radio_button_toggled(checked, "on"))
        #information CheckBox
        # self.ui_ImageView.cBox_classname.stateChanged.connect(lambda: self.BboxDraw_on_radio_button_toggled("output", "output"))
        # self.ui_ImageView.cBox_score.stateChanged.connect(lambda: self.BboxDraw_on_radio_button_toggled("output", "output"))

        # previous, next btn
        self.ui_ImageView.pushButton.clicked.connect(self.prev_image)
        self.ui_ImageView.pushButton_2.clicked.connect(self.next_image)
        self.ui_ImageView.pushButton.setShortcut("q")   # 이전 버튼에 'q' 단축키 지정
        self.ui_ImageView.pushButton_2.setShortcut("w")   # 다음 버튼에 'w' 단축키 지정

        # select table widget
        #self.ui_ImageView.tableWidget_FileList.cellClicked.connect(self.get_selected_item)


        
    def open_btn_PloygonDraw_window(self):
        dialog = QDialog()
        ui = Ui_PolygonDraw()
        ui.setupUi(dialog)
        dialog.exec()
    
    def open_btn_DataAnalysis_window(self):
        dialog = QDialog()
        ui = Ui_DataAnalysis()
        ui.setupUi(dialog)
        dialog.exec()
    
    def open_btn_DataCheck_window(self):
        dialog = QDialog()
        ui = Ui_DatasetCheck()
        ui.setupUi(dialog)
        dialog.exec()
#----------------------------file Open browser----------------------------#
    def browse_folder(self, text_edit):
        dialog_title = text_edit.objectName().replace('textEdit','Open')
        # 폴더 탐색기 열기
        folder_path = QFileDialog.getExistingDirectory(
            None,
            dialog_title,  # 다이얼로그 제목
            ""  # 초기 경로 (빈 문자열이면 현재 디렉터리)
        )
        if folder_path:  # 폴더를 선택한 경우
            text_edit.setText(folder_path)

#----------------------------Data Flip Function----------------------------#
    #GT Flip Func
    def gt_flip(self, gt_input_path,image_width,output_path):
        try:
            count_var = 0 # flip된 파일 개수 확인 변수
            gt_list = os.listdir(gt_input_path) #gt 목록 가져오기
            
            for filename in gt_list:
                flipped_lines = [] # flip된 gt 저장할 리스트
                gt_path = os.path.join(gt_input_path, filename)
                #Text file만 처리
                if filename.lower().endswith(('.txt')):
                    with open(gt_path,'r') as fopen:
                        gt_lines = fopen.readlines()

                        for gt_line in gt_lines:
                            coords = re.split(r'[,\s]+', gt_line.strip())
                            #ncn Dataset 기본 포맷
                            if len(coords) == 5:
                                classname = coords[0]
                                x1,y1,x2,y2 = coords[1:5]
                            #학습 후, confidence socre 포함된 포맷
                            elif len(coords) == 6:
                                classname = coords[0]
                                score = coords[1]
                                x1,y1,x2,y2 = coords[2:6]
                            #잘못된 형식
                            else:
                                raise ValueError(f"GT 파일 형식 확인 필요")

                            fliped_x1 = int(image_width) - int(x2)
                            fliped_x2 = int(image_width) - int(x1)
                            #ncn Dataset 기본 포맷
                            if len(coords) == 5:
                                flipped_bbox = (classname,fliped_x1,y1,fliped_x2,y2)
                            #학습 후, confidence socre 포함된 포맷
                            elif len(coords) == 6:
                                flipped_bbox = (classname,score,fliped_x1,y1,fliped_x2,y2)

                            flipped_line = ",".join(map(str,flipped_bbox)) + "\n"
                            flipped_lines.append(flipped_line)
                        count_var += 1

                    gt_output_full_path = os.path.join(output_path,'output_gt')
                    #output 폴더 없을 경우 생성
                    if not os.path.exists(gt_output_full_path):
                        os.makedirs(gt_output_full_path)

                    flipped_gt_output_path = os.path.join(gt_output_full_path,filename)
                    with open(flipped_gt_output_path,'w') as wopen:
                        wopen.writelines(flipped_lines)

            return count_var

        except Exception as e:
            QMessageBox.critical(None, "Error", f"GT 처리 중 오류가 발생했습니다.\n{str(e)}")

    #Image Flip Func
    def image_flip(self, image_input_path,output_path):
        try:
            count_var = 0
            image_list = os.listdir(image_input_path)
            for filename in image_list:
                image_path = os.path.join(image_input_path, filename)
                # 이미지 파일만 처리
                if filename.lower().endswith(('.png', '.jpg')):
                    with Image.open(image_path) as img:
                        flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)
                        image_output_full_path = os.path.join(output_path,'output_image')
                        #output 폴더 없을 경우 생성
                        if not os.path.exists(image_output_full_path):
                            os.makedirs(image_output_full_path)
                        flipped_image_output_path = os.path.join(image_output_full_path, filename)
                        flipped_img.save(flipped_image_output_path)
                        count_var += 1
            return count_var
        except Exception as e:
            QMessageBox.critical(None, "Error", f"이미지 처리 중 오류가 발생했습니다.\n{str(e)}")

    #Data Flip main Func
    def Data_flip(self, ui):
        gt_input_path = ui.gt_textEdit.toPlainText().strip()
        image_width = ui.image_width_textEdit.toPlainText().strip()
        image_input_path = ui.image_textEdit.toPlainText().strip()
        output_path = ui.output_textEdit.toPlainText().strip()

        # 경로 검증
        if not os.path.exists(gt_input_path) and not os.path.exists(image_input_path):
            QMessageBox.critical(None, "Error", "Image/GT 경로가 유효하지 않습니다.")
            return
        if image_width == '':
            QMessageBox.critical(None, "Error", "Image Width를 입력해주세요")
            return
        if not os.path.isdir(output_path):
            QMessageBox.critical(None, "Error", "Output 경로가 유효하지 않습니다.")
            return
        try:
            #Image 경로만 입력한 경우
            if gt_input_path == '':
                image_count_var = self.image_flip(image_input_path,output_path)
                QMessageBox.information(None, "Success", f"-----Data Flip 완료-----\nImage : {image_count_var}개")
            #GT 경로만 입력한 경우
            elif image_input_path == '':
                gt_count_var = self.gt_flip(gt_input_path,image_width,output_path)
                QMessageBox.information(None, "Success", f"-----Data Flip 완료-----\nGT : {gt_count_var}개")
            #GT/image 경로 모두 입력한 경우
            else:
                image_count_var = self.image_flip(image_input_path,output_path)
                gt_count_var = self.gt_flip(gt_input_path,image_width,output_path)
                QMessageBox.information(None, "Success", f"-----Data Flip 완료-----\nGT : {gt_count_var}개\nImage : {image_count_var}개")

        except Exception as e:
            QMessageBox.critical(None, "Error", f"처리 중 오류가 발생했습니다.\n{str(e)}")

#----------------------------Data FileRename Function----------------------------#
    def Rename_on_radio_button_toggled(self, checked, option,ui):
        if checked:
            self.rename_selected_option = option  # 선택된 옵션을 클래스 속성에 저장
        if self.rename_selected_option == "PartRename":
            ui.textEdit_OldString.setEnabled(True)
        else:
            ui.textEdit_OldString.setEnabled(False)
            ui.textEdit_OldString.clear()  # 텍스트가 있으면 지워줍니다.
    
    def Data_Rename(self,ui):
        input_path_1 = ui.textEdit_input_path1.toPlainText().strip()
        input_path_2 = ui.textEdit_input_path2.toPlainText().strip()
        replace_old_string = ui.textEdit_OldString.toPlainText().strip()
        replace_new_string = ui.textEdit_NewString.toPlainText().strip()

        if not os.path.exists(input_path_1):
            QMessageBox.critical(None,"Error","Primary 경로는 필수로 입력해주세요.")
            return

        if replace_new_string == '':
            QMessageBox.critical(None,"Error","변경/추가할 String을 입력하세요")
            return

        try:
            if self.rename_selected_option == 'AllRename':
                if input_path_2 == '':
                    self.Rename_String(ui,replace_new_string,input_path_1)
                else:
                    self.Rename_String(ui,replace_new_string,input_path_1,input_path_2)

            elif self.rename_selected_option == 'PartRename':
                if input_path_2 == '':
                    self.Replace_String(ui,replace_old_string,replace_new_string,input_path_1)
                else:
                    self.Replace_String(ui,replace_old_string,replace_new_string,input_path_1,input_path_2)

            elif self.rename_selected_option == 'front' or self.rename_selected_option == 'rear':
                if input_path_2 == '':
                    self.Insert_String(ui,replace_new_string,input_path_1)
                else:
                    self.Insert_String(ui,replace_new_string,input_path_1,input_path_2)
            else:
                raise ValueError(f"Error Radio Button")

        except Exception as e:
            QMessageBox.critical(None, "Error", f"처리 중 오류가 발생했습니다.\n{str(e)}")
    
    def Rename_String(self,ui,string,input_path_1,input_path_2=None):
        mode_type = False
        path_1_list = natsorted(os.listdir(input_path_1))

        if input_path_2:
            path_2_list = natsorted(os.listdir(input_path_2))
            mode_type = True

            if len(path_1_list) != len(path_2_list):
                QMessageBox.critical(None,"Error","두 경로의 파일 개수 다름")
                return
            basename_2 = {os.path.splitext(f)[0]: f for f in path_2_list}
        try:
            # 동일한 인덱스로 파일명 변경
            for idx, filename_1 in enumerate(path_1_list, start=1):
                # Path1 파일 변경
                name_1, ext_1 = os.path.splitext(filename_1)
                new_filename = f"{string}{str(idx).zfill(4)}{ext_1}"
                old_path_1 = os.path.join(input_path_1, filename_1)
                new_path_1 = os.path.join(input_path_1, new_filename)
                os.rename(old_path_1, new_path_1)

                # Path2 파일 변경 (mode가 True일 때만 실행)
                if mode_type and name_1 in basename_2:
                    old_path_2 = os.path.join(input_path_2, basename_2[name_1])  # 기존 파일명 가져오기
                    ext_2 = os.path.splitext(basename_2[name_1])[1]
                    new_path_2 = os.path.join(input_path_2, f"{string}{str(idx).zfill(4)}{ext_2}")
                    os.rename(old_path_2, new_path_2)

                progress = int(idx / len(path_1_list) * 100)
                ui.progressBar.setValue(progress)

            if mode_type:#path1,2일때
                QMessageBox.information(None, "Success", f"-----Rename-----\nPrimary : {len(path_1_list)}개\nSecondary : {len(path_2_list)}개")
            else:
                QMessageBox.information(None, "Success", f"-----Rename-----\nPrimary : {len(path_1_list)}개")
            

        except Exception as e:
            QMessageBox.critical(None, "Error", f"파일명 변경 중 오류가 발생했습니다.\n{str(e)}")
            
    def Replace_String(self,ui,old_string,new_string,input_path_1,input_path_2=None):
        mode_type = False
        path_1_list = natsorted(os.listdir(input_path_1))
        total_steps = len(path_1_list)

        if input_path_2:
            path_2_list = natsorted(os.listdir(input_path_2))
            mode_type = True
            if len(path_1_list) != len(path_2_list):
                QMessageBox.critical(None,"Error","두 경로의 파일 개수 다름")
                return
            total_steps += len(path_2_list)
        try:
            # 이미 처리한 작업 카운트
            current_step = 0
            #path1 파일 치환
            for idx, filename_1 in enumerate(path_1_list,start=1):
                if old_string in filename_1:
                    new_filename_1 = filename_1.replace(old_string,new_string)
                    old_path_1 = os.path.join(input_path_1, filename_1)
                    new_path_1 = os.path.join(input_path_1,new_filename_1)
                    os.rename(old_path_1,new_path_1)
                current_step += 1
                progress = int(current_step / total_steps * 100)
                ui.progressBar.setValue(progress)
            #path2 파일 치환
            if mode_type:
                for idx2, filename_2 in enumerate(path_2_list,start=1):
                    if old_string in filename_2:
                        new_filename_2 = filename_2.replace(old_string,new_string)
                        old_path_2 = os.path.join(input_path_2, filename_2)
                        new_path_2 = os.path.join(input_path_2,new_filename_2)
                        os.rename(old_path_2,new_path_2)
                    current_step += 1
                    progress = int(current_step / total_steps * 100)
                    ui.progressBar.setValue(progress)
                QMessageBox.information(None, "Success", f"-----Replace-----\nPrimary : {str(idx)}개\nSecondary : {str(idx2)}개")
            else:
                QMessageBox.information(None, "Success", f"-----Replace-----\nPrimary : {str(idx)}개\n")
        except Exception as e:
            QMessageBox.critical(None, "Error", f"파일명 치환 중 오류가 발생했습니다.\n{str(e)}")
    
    def Insert_String(self,ui,new_string,input_path_1,input_path_2=None):
        mode_type = False
        path_1_list = natsorted(os.listdir(input_path_1))
        total_steps = len(path_1_list)

        if input_path_2:
            path_2_list = natsorted(os.listdir(input_path_2))
            mode_type = True
            if len(path_1_list) != len(path_2_list):
                QMessageBox.critical(None,"Error","두 경로의 파일 개수 다름")
                return
            total_steps += len(path_2_list)
        try:
            # 이미 처리한 작업 카운트
            current_step = 0
            #앞에 추가
            if self.rename_selected_option == 'front':
                for idx_1, filename_1 in enumerate(path_1_list,start=1):
                    basename_1, ext_1 = os.path.splitext(filename_1)
                    new_filename_1 = f"{new_string}{basename_1}{ext_1}"
                    old_path_1 = os.path.join(input_path_1, filename_1)
                    new_path_1 = os.path.join(input_path_1,new_filename_1)
                    os.rename(old_path_1,new_path_1)
                    current_step += 1
                    progress = int(current_step / total_steps * 100)
                    ui.progressBar.setValue(progress)
                if mode_type:
                    for idx_2, filename_2 in enumerate(path_2_list,start=1):
                        basename_2, ext_2 = os.path.splitext(filename_2)
                        new_filename_2 = f"{new_string}{basename_2}{ext_2}"
                        old_path_2 = os.path.join(input_path_2, filename_2)
                        new_path_2 = os.path.join(input_path_2,new_filename_2)
                        os.rename(old_path_2,new_path_2)
                        current_step += 1
                        progress = int(current_step / total_steps * 100)
                        ui.progressBar.setValue(progress)
                    QMessageBox.information(None, "Success", f"----- prepend-----\nPrimary : {str(idx_1)}개\nSecondary : {str(idx_2)}개")
                else:
                    QMessageBox.information(None, "Success", f"----- prepend-----\nPrimary : {str(idx_1)}개\n")
            #뒤에 추가
            if self.rename_selected_option == 'rear':
                for idx_1, filename_1 in enumerate(path_1_list,start=1):
                    basename_1, ext_1 = os.path.splitext(filename_1)
                    new_filename_1 = f"{basename_1}{new_string}{ext_1}"
                    old_path_1 = os.path.join(input_path_1, filename_1)
                    new_path_1 = os.path.join(input_path_1,new_filename_1)
                    os.rename(old_path_1,new_path_1)
                    current_step += 1
                    progress = int(current_step / total_steps * 100)
                    ui.progressBar.setValue(progress)
                if mode_type:
                    for idx_2, filename_2 in enumerate(path_2_list,start=1):
                        basename_2, ext_2 = os.path.splitext(filename_2)
                        new_filename_2 = f"{basename_2}{new_string}{ext_2}"
                        old_path_2 = os.path.join(input_path_2, filename_2)
                        new_path_2 = os.path.join(input_path_2,new_filename_2)
                        os.rename(old_path_2,new_path_2)
                        current_step += 1
                        progress = int(current_step / total_steps * 100)
                        ui.progressBar.setValue(progress)
                    QMessageBox.information(None, "Success", f"----- append-----\nPrimary : {str(idx_1)}개\nSecondary : {str(idx_2)}개")
                else:
                    QMessageBox.information(None, "Success", f"----- append-----\nPrimary : {str(idx_1)}개\n")
        except Exception as e:
            QMessageBox.critical(None, "Error", f"파일명 추가 중 오류가 발생했습니다.\n{str(e)}")

#----------------------------Image View Function----------------------------#
    def view_on_radio_button_toggled(self, checked, option):
        if checked:
            self.ImageView_selected_option_view = option  
    
    def box_on_radio_button_toggled(self, checked, option):
        if checked:
            self.ImageView_selected_option_onoff = option  

    def open_folder(self, path_type: str, folder_type: str):
        title = f"Select {path_type.capitalize()} Path {folder_type} Folder"
        # self 대신 부모 위젯인 self.main_window 전달
        folder = QFileDialog.getExistingDirectory(self.ImageView_window, title, "")
        if folder:
            if path_type == "first": # path 1 선택 했을 경우
                if folder_type == "GT": # path 1 의 GT를 선택했을 경우
                    self.first_gt_path = None 
                    self.first_gt_path = folder
                    if self.first_image_path is None: # path 1 의 GT를 선택했는데 Image가 없을 경우
                        self.open_folder("first", "Image")
                else: # path 1의 Image를 선택했을 경우
                    self.first_image_path = None
                    self.first_image_path = folder
                    self.first_image_list = self.load_image(folder)
                self.populate_file_table(path_type)
                self.display_image(path_type)

            elif path_type == "second": # path 2 선택 했을 경우
                if folder_type == "GT": # path 2 의 GT를 선택했을 경우
                    self.second_gt_path = None
                    self.second_gt_path = folder
                    if self.second_image_path is None: # path 2 의 GT를 선택했는데 Image가 없을 경우
                        self.open_folder("second", "Image")
                else:  # path 2의 Image를 선택했을 경우
                    self.second_image_path = None
                    self.second_image_path = folder
                    self.second_image_list = self.load_image(folder)
                self.populate_file_table(path_type)
                self.display_image(path_type)
            else: # ouput path를 선택했을 경우
                self.ouput_path = folder

    def load_image(self, folder):
        valid_extensions = ('.png','.jpg')
        image_files = [f for f in natsorted(os.listdir(folder)) if f.lower().endswith(valid_extensions)]
        return image_files

    def display_image(self, path_type):
        if path_type == 'first':
            if not self.first_image_list:
                self.ui_ImageView.label_ImageView_1.setText('No images')
                return
            image_path = os.path.join(self.first_image_path,self.first_image_list[self.first_current_index])
            pixmap = QPixmap(image_path)
            if pixmap.isNull():
                self.ui_ImageView.label_ImageView_1.setText("Error Loading Image")
            else:
                self.ui_ImageView.label_ImageView_1.setPixmap(pixmap)
                self.ui_ImageView.label_ImageView_1.setScaledContents(True)
        elif path_type == 'second':
            if not self.second_image_list:
                self.ui_ImageView.label_ImageView_2.setText('No images')
                return
            image_path = os.path.join(self.second_image_path, self.second_image_list[self.second_current_index])

            pixmap = QPixmap(image_path)
            if pixmap.isNull():
                self.ui_ImageView.label_ImageView_2.setText("Error Loading Image")
            else:
                self.ui_ImageView.label_ImageView_2.setPixmap(pixmap)
                self.ui_ImageView.label_ImageView_2.setScaledContents(True)
        else:
            if not self.first_image_list:
                self.ui_ImageView.label_ImageView_1.setText('No images')
            if not self.second_image_list:
                self.ui_ImageView.label_ImageView_2.setText('No images')
                return
            image_path_1 = os.path.join(self.first_image_path, self.first_image_list[self.first_current_index])
            image_path_2 = os.path.join(self.second_image_path, self.first_image_list[self.first_current_index])
            #image_path_2 = os.path.join(self.second_image_path, self.second_image_list[self.second_current_index])

            pixmap_1 = QPixmap(image_path_1)
            pixmap_2 = QPixmap(image_path_2)
            if pixmap_1.isNull():
                self.ui_ImageView.label_ImageView_1.setText("Error path 1 Loading Image")
            if  pixmap_2.isNull():
                self.ui_ImageView.label_ImageView_1.setPixmap(pixmap_1)
                self.ui_ImageView.label_ImageView_1.setScaledContents(True)
                self.ui_ImageView.label_ImageView_2.setText("Not path 2 Loading Image")
            else:
                self.ui_ImageView.label_ImageView_1.setPixmap(pixmap_1)
                self.ui_ImageView.label_ImageView_1.setScaledContents(True)

                self.ui_ImageView.label_ImageView_2.setPixmap(pixmap_2)
                self.ui_ImageView.label_ImageView_2.setScaledContents(True)

    def next_image(self):
        if self.ImageView_selected_option_view == 'dual':
            if self.first_image_list and self.first_current_index < len(self.first_image_list) -1:# and self.second_image_list and self.second_current_index < len(self.second_image_list) -1:
                self.first_current_index += 1
                self.second_current_index = self.first_current_index
                self.display_image('dual')

        elif self.ImageView_selected_option_view == 'first':
            if self.first_image_list and self.first_current_index < len(self.first_image_list) -1:
                self.first_current_index += 1
                self.display_image('first')

        elif self.ImageView_selected_option_view == 'second':
            if self.second_image_list and self.second_current_index < len(self.second_image_list) -1:
                self.second_current_index += 1
                
                self.display_image('second')

    def prev_image(self):
        if self.ImageView_selected_option_view == 'dual':
            if self.first_current_index > 0 and self.second_current_index > 0 :
                self.first_current_index -= 1
                self.second_current_index = self.first_current_index
                self.display_image('dual')

        elif self.ImageView_selected_option_view == 'first':
            if self.first_current_index > 0 :
                self.first_current_index -= 1
                self.display_image('first')

        elif self.ImageView_selected_option_view == 'second':
            if self.second_current_index > 0 :
                if self.second_current_index > len(self.second_image_list):
                    self.second_current_index = len(self.second_image_list)
                self.second_current_index -= 1

                self.display_image('second')
    
    def get_selected_item(self, row, column):
        item = self.ui_ImageView.tableWidget_FileList.item(row, column)
        if item:  # 선택된 항목이 있는지 확인
            selected_value = item.text()
            print(f"선택된 값: {selected_value}")
        


    def populate_file_table(self,type):
        if type == 'first':
            table_widget = self.ui_ImageView.tableWidget_Path1_FileList
            files = self.first_image_list
            header_label = "Path 1 File Name"
        elif type == 'second':
            table_widget = self.ui_ImageView.tableWidget_Path2_FileList
            files = self.second_image_list
            header_label = "Path 2 File Name"
        else:
            print("잘못된 type 값. ('first' 또는 'second' 사용)")
            return

        table_widget.clear()
        table_widget.setRowCount(0)
        table_widget.setColumnCount(1)
        table_widget.setHorizontalHeaderLabels([header_label])


        table_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)


        for row, filename in enumerate(files):
            table_widget.insertRow(row)
            item = QTableWidgetItem(filename)
            table_widget.setItem(row, 0, item)

        '''if type == 'first':
            self.ui_ImageView.tableWidget_Path1_FileList.clear()
            self.ui_ImageView.tableWidget_Path1_FileList.setRowCount(0)
            self.ui_ImageView.tableWidget_Path1_FileList.setColumnCount(1)
            self.ui_ImageView.tableWidget_Path1_FileList.setHorizontalHeaderLabels(["Path 1 File Name"])

            self.ui_ImageView.tableWidget_Path1_FileList.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

            row = 0
            files = self.first_image_list
            for filename in files:
                self.ui_ImageView.tableWidget_Path1_FileList.insertRow(row)
                item = QTableWidgetItem(filename)
                self.ui_ImageView.tableWidget_Path1_FileList.setItem(row, 0, item)
                row += 1
        elif type == 'second':
            self.ui_ImageView.tableWidget_Path2_FileList.clear()
            self.ui_ImageView.tableWidget_Path2_FileList.setRowCount(0)
            self.ui_ImageView.tableWidget_Path2_FileList.setColumnCount(1)
            self.ui_ImageView.tableWidget_Path2_FileList.setHorizontalHeaderLabels(["path 2 File Name"])
    
            self.ui_ImageView.tableWidget_Path2_FileList.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
    
            row = 0
            files = self.second_image_list
            for filename in files:
                self.ui_ImageView.tableWidget_Path2_FileList.insertRow(row)
                item = QTableWidgetItem(filename)
                self.ui_ImageView.tableWidget_Path2_FileList.setItem(row, 0, item)
                row += 1'''
