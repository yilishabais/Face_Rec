import remi.gui as gui
import Service.Access as A
from remi import start, App
class MyApp(App):
    def __init__(self, *args):
        super(MyApp, self).__init__(*args)

    def main(self):
        #creating a container VBox type, vertical
        wid = gui.VBox(width=1000, height=600, style={'margin':'5px auto', 'padding': '10px'})

        #creating a text label, "white-space":"pre" preserves newline
        self.lbl1 = gui.Label('人脸匹配检测', width='80%', height='50%', style={"white-space": "pre"})
        self.lbl2 = gui.Label('选择匹配图片', width='80%', height='50%', style={"white-space": "pre"})
        self.lbl3 = gui.Label('选择匹配类型', width='80%', height='50%')
        self.img = gui.Image('/res:logo.png', height=100, margin='10px')
        self.img.onclick.do(self.on_img_clicked)
        #a button for simple interaction
        bt = gui.Button('开始匹配', width=200, height=30)

        #setting up the listener for the click event
        bt.onclick.do(self.on_button_pressed)
        comboAlignItems = gui.DropDown.new_from_list(('证件照', '生活照', '摄像头识别'),
                                                     style='left:160px; position:absolute; top:100px; width:152px; height: 30px')

        #adding the widgets to the main container
        wid.append(self.lbl1)
        wid.append(self.lbl3)
        wid.append(comboAlignItems)
        wid.append(self.lbl2)
        wid.append(bt)

        # returning the root widget
        return wid

    # listener function
    def on_button_pressed(self, emitter):
        img1 = "/Users/zhaoliang/Downloads/Face_Img/pic1.jpg"
        img2 = "/Users/zhaoliang/Downloads/Face_Img/pic2.jpg"
        flag = A.result(img1, img2)
        if(flag):
            self.lbl.set_text('OK')
        else:
            self.lbl.set_text('NO')

    # 更换匹配图片
    def on_img_clicked(self,widget):
        self.lbl.set_text('Image clicked!')

if __name__ == "__main__":
    # starts the webserver
    # optional parameters
    # start(MyApp,address='127.0.0.1', port=8081, multiple_instance=False,enable_file_cache=True, update_interval=0.1, start_browser=True)
    start(MyApp, debug=False, address='0.0.0.0', port=0)
