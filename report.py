class Report:
    def __init__(self, content_width: int = 0):
        self.__content_width = content_width
        self.__report_content: list[str] = []

        self.add_line_fill("BOOKBOT", "=")
        self.__end = "\n " + self.__line_fill("END", "=")

    def add_line(self, line: str, space_before: bool = False):
        if space_before:
            self.__report_content.append(f"\n {line}")
            return
        self.__report_content.append(f" {line}")

    def add_line_fill(self, line: str, fill_char: str = "-"):
        self.add_line(self.__line_fill(line, fill_char), True)

    def __line_fill(self, line: str, fill_char: str):
        fill_size = self.__fill_size(line)

        if len(fill_char) != 1 or fill_size <= 1:
            return line

        line = f" {line} "

        if fill_size % 2 != 0:
            line += " "

        if fill_size <= 3:
            return line

        part_size = self.__fill_size(line) // 2
        return f"{fill_char * part_size}{line}{fill_char * part_size}"

    def __fill_size(self, line: str):
        return self.__content_width - len(line)

    def get_text(self):
        return "\n".join(self.__report_content) + self.__end
