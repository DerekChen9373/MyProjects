import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):

    return GRAPH_MARGIN_SIZE+year_index*((width-2*GRAPH_MARGIN_SIZE)/len(YEARS))

def draw_fixed_lines(canvas):

    canvas.delete('all')
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    for i in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(1000, i), GRAPH_MARGIN_SIZE/2, get_x_coordinate(1000, i), CANVAS_HEIGHT-GRAPH_MARGIN_SIZE/2)
        canvas.create_text(get_x_coordinate(1000, i)+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)

def draw_names(canvas, name_data, lookup_names):

    draw_fixed_lines(canvas)
    a1=GRAPH_MARGIN_SIZE
    d=(CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)/MAX_RANK
    for i in range(len(lookup_names)):
        for j in range(len(YEARS)-1):
            color=COLORS[i % len(COLORS)]
            name=lookup_names[i].strip()
            if name in name_data:
                if str(YEARS[j]) in name_data[name]:
                    if str(YEARS[j + 1]) in name_data[name]:
                        x1, x2 = get_x_coordinate(CANVAS_WIDTH, j),get_x_coordinate(CANVAS_WIDTH, j+1)
                        y1, y2 = a1+(float(name_data[name][str(YEARS[j])]))*d, a1+(float(name_data[name][str(YEARS[j + 1])]))*d
                        rank1, rank2=name_data[name][str(YEARS[j])], name_data[name][str(YEARS[j + 1])]
                    else:
                        x1, x2 = get_x_coordinate(CANVAS_WIDTH, j), get_x_coordinate(CANVAS_WIDTH, j + 1)
                        y1, y2 = a1 + (float(name_data[name][str(YEARS[j])])) * d,CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
                        rank1, rank2 = name_data[name][str(YEARS[j])], '*'
                else:
                    if str(YEARS[j+1]) in name_data[name]:
                        x1, x2 = get_x_coordinate(CANVAS_WIDTH, j), get_x_coordinate(CANVAS_WIDTH, j + 1)
                        y1, y2 =CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, a1 + (float(name_data[name][str(YEARS[j + 1])])) * d
                        rank1, rank2 = "*", name_data[name][str(YEARS[j + 1])]
                    else :
                        x1, x2 = get_x_coordinate(CANVAS_WIDTH, j), get_x_coordinate(CANVAS_WIDTH, j + 1)
                        y1, y2 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                        rank1, rank2 = "*", "*"
            else:
                x1, x2=get_x_coordinate(CANVAS_WIDTH, j),get_x_coordinate(CANVAS_WIDTH, j+1)
                y1, y2=CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
                rank1, rank2="*", "*"
            canvas.create_line(x1, y1, x2, y2, width=LINE_WIDTH, fill=color)
            canvas.create_text(x1+ TEXT_DX,y1, text=name + rank1, anchor=tkinter.SW, fill=color)
            canvas.create_text(x2 + TEXT_DX, y2, text=name + rank2, anchor=tkinter.SW, fill=color)

def main():

    name_data = babynames.read_files(FILENAMES)
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)
    draw_fixed_lines(canvas)
    top.mainloop()


if __name__ == '__main__':
    main()
