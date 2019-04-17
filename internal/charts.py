import pygal
import pdb

class PieChart():
    def __init__(self, name, **kwargs):
        self.chart = pygal.Pie(**kwargs)
        self.chart.title = name

    def generate(self, chart_data):
        # Add data to chart
        for key, value in chart_data.items():
            self.chart.add(key, value)

        # Return the rendered SVG
        return self.chart.render(is_unicode=True)

class BarChart():
    def __init__(self, name, **kwargs):
        self.chart = pygal.Bar(**kwargs)
        self.chart.title = name

    def generate(self, chart_data):
        # Add data to chart
        for key, value in chart_data.items():
            self.chart.add(key, value)

        # Return the rendered SVG
        return self.chart.render(is_unicode=True)