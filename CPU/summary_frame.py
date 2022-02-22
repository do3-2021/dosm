from tkinter import tk
from home import mini_frame
from . import graph
from .cpu_data.global_cpu import GlobalCPU


class SummaryFrame(mini_frame.MiniFrame):
    def __init__(self, master, logger, **options):
        super().__init__(master, logger, **options)
        self.cpu = GlobalCPU()
        self.cpuUsageGraph = graph.LineGraph(self)

    def show(self):
        self.cpuUsageGraph = graph.LineGraph(self,width=40, padx=40, pady=40)
        self.cpuUsageGraph.pack(fill=tk.BOTH)
        self.cpuUsageGraph.show()

    def hide(self):
        self.grid_forget()

    def update(self):
        self.cpu.update()
        self.cpuUsageGraph.redraw(self.cpu.usages)
