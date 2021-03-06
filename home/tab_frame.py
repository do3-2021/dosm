from tkinter import Frame
from utils import parallel_run
from integrator import base_frame
from home import base_summary_frame
from config import NB_OF_MINI_FRAME

from connected_users import summary_frame as cu_frame
from cpu import summary_frame as cpu_frame
from ipc import summary_frame as ipc_frame
from login_history import summary_frame as login_history_frame
from memory import summary_frame as memory_frame
from net import summary_frame as net_frame
from ports import summary_frame as ports_frame
from process import summary_frame as process_frame


class TabFrame(base_frame.BaseFrame):
    def __init__(self, master, logger, **options):
        super().__init__(master, logger, **options)
        self.logger = logger
        self.summary_frames = []
        self.name = 'Home'
        self.grid_frame = Frame(self)
        
    def show(self):
        self.summary_frames = [
            ipc_frame.SummaryFrame(self.grid_frame, self.logger, 'IPC'),
            cpu_frame.SummaryFrame(self.grid_frame, self.logger, 'CPU'),
            cu_frame.SummaryFrame(self.grid_frame, self.logger, 'CU'),
            net_frame.SummaryFrame(self.grid_frame, self.logger, 'NET'),
            ports_frame.SummaryFrame(self.grid_frame, self.logger, 'PORTS'),
            login_history_frame.SummaryFrame(self.grid_frame, self.logger, 'LOGIN_HISTORY'),
            process_frame.SummaryFrame(self.grid_frame, self.logger, 'PROCESS'),
            memory_frame.SummaryFrame(self.grid_frame, self.logger, 'MEMORY'),
            base_summary_frame.EmptySummaryFrame(self.grid_frame, self.logger, 'DISK'),
        ]
        
        for summary_frame in self.summary_frames:
            parallel_run(summary_frame.show, lambda x: None)

        # fill the grid
        index = 0
        for r in range(3):
            for c in range(3):
                self.summary_frames[index].grid(row=r, column=c, padx=10, pady=10, sticky="nsew")
                index += 1
                self.grid_frame.grid_rowconfigure(r, weight=1)
                self.grid_frame.grid_columnconfigure(c, weight=1)

        self.grid_frame.pack(fill="both", expand=True)

    def update(self, dt):
        for summary_frame in self.summary_frames:
            summary_frame.update(dt)

    def hide(self):
        for summary_frame in self.summary_frames:
            summary_frame.hide()
        self.grid_frame.destroy()
