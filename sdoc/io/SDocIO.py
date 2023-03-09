from cleo.io.io import IO


class SDocIO(IO):
    """
    IO object with title.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def title(self, message: str) -> None:
        """
        Writes a title to the output.

        :param str message: The title of a section.
        """
        self.write_line(['<title>%s</>' % message,
                         '<title>%s</>' % ('=' * len(message)),
                         ''])

# ----------------------------------------------------------------------------------------------------------------------
