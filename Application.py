
import tkinter as tk
import views.view as _view_
import models.Video as _Video_
import controllers.Controller as _Controller_


class Application(tk.Tk):

    def __init__(self):

        super().__init__()
        self.title('Video Tracker')
        # create a video model
        video = _Video_.Video()
        # create a view and place it on the root window
        view = _view_.View(self)

        # create a controller
        controller = _Controller_.Controller(self, video, view)

        # set the controller to view
        view.setController(controller)
        

if __name__ == '__main__':
    app = Application()
    app.mainloop()

