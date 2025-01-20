from PySide6.QtWidgets import QMainWindow, QDialog, QFileDialog

from UI.Main_window_ui import Ui_MainWindow  # Main_window.py
from UI.btn_DataFlip_ui import Ui_Dialog_DataFlip as Ui_DataFlip # Data Flip Dialog
from UI.btn_FileRename_ui import Ui_Dialog_FileRename as Ui_FileRename # Data File Rename Dialog
from UI.btn_BboxDraw_ui import Ui_Dialog_BboxDraw as Ui_BboxDraw # Bounding Box Drawing Dialog
from UI.btn_PloygonDraw_ui import Ui_Dialog_PolygonDraw as Ui_PolygonDraw # Ploygon Drawing Dialog
from UI.btn_DataAnalysis_ui import Ui_Dialog_DataAnalysis as Ui_DataAnalysis # Ploygon Drawing Dialog
from UI.btn_DatasetCheck_ui import Ui_Dialog_DatasetCheck as Ui_DatasetCheck # Ploygon Drawing Dialog


from UI.madeBy_ui import Ui_Dialog as Ui_madeBy  

from PySide6.QtWidgets import QMainWindow, QDialog, QMessageBox
from PySide6.QtGui import QImageReader, QPixmap

import os
import re
from PIL import Image  # Pillow 라이브러리 사용


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
        self.ui.btn_BboxDraw.clicked.connect(self.open_btn_BboxDraw_window)
        self.ui.btn_PolygonDraw.clicked.connect(self.open_btn_PloygonDraw_window)
        self.ui.btn_DataAnalysis.clicked.connect(self.open_btn_DataAnalysis_window)
        self.ui.btn_DataCheck.clicked.connect(self.open_btn_DataCheck_window)

    def run(self):
        # 메인 창 실행
        self.main_window.show()
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
        dialog.exec()

    def open_btn_FileRename_window(self):
        dialog = QDialog()
        ui = Ui_FileRename()
        ui.setupUi(dialog)
        dialog.exec()

    def open_btn_BboxDraw_window(self):
        dialog = QDialog()
        ui = Ui_BboxDraw()
        ui.setupUi(dialog)
        dialog.exec()
    
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