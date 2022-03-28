from manim import *

class Einleitung(Scene):
    def construct(self):
        author = Text("Fabus",font_size=11, color=RED)
        author.to_corner(DR)
        course = Text("V1G1 - Analyis 1",font_size=11, color=YELLOW)
        course.to_corner(DL)
        title = Text("Grundlagen")
        basel = Text("Aussagenlogik")
        VGroup(title, basel).arrange(DOWN)
        self.wait(1)
        self.play(Write(course))
        self.add(author)
        self.wait(1)
        self.play(
            Write(title),
        )
        self.wait(4)
        self.play(FadeIn(basel, shift=DOWN),)
        self.wait(3)

        transform_title = Text("Aussage")
        transform_title.to_corner(UP + LEFT)
        self.play(
            Transform(title, transform_title),
            LaggedStart(*[FadeOut(obj, shift=DOWN) for obj in basel]),
        )
        aussage = Text("- mathematischer oder sprachlicher Satz \n- wahr oder falsch")
        beispiel = Text("Beispiele", font_size=32)
        beispiel.to_corner(UP+ LEFT)
        self.play(Write(aussage),)
        self.wait(4)
        self.play(
            FadeOut(aussage),
            LaggedStart(*[Transform(title, beispiel)]),
        )
        self.wait(1)
        aussagen = MarkupText(
            f'-7+8= 14 <span fgcolor="{RED}">\n- Paris ist eine schöne Stadt</span>', color=GREEN
        )
        self.play(Write(aussagen))
        self.wait(5)
        self.play(FadeOut(title),
        FadeOut(aussagen))
        junktoren = Text("Junktoren")
        self.play(Write(junktoren))
        self.wait(2)
        transform_title = Text("Junktoren")
        transform_title.to_corner(UP + LEFT)
        self.play(Transform(junktoren, transform_title),)

        table = r"""
        \begin{table}[]
        \centering
        \begin{tabular}{|l|l|l|}\hline
        Gesprochen & Symbol & Name   \\\hline
        "nicht A" & $\neg A$ & \emph{Negation}  \\
        "A und B" & $A \wedge B$ & \emph{Konjunktion}\\
        "A oder B" & $A \vee B$ & \emph{Disjunktion}\\
        "A impliziert B" & $A \implies B$ & \emph{Implikation} \\
        "A gdw. B" & $A \iff B$ & \emph{Äquivalenz}    \\\hline
        \end{tabular}
        \end{table}
        """
        tex_table = Tex(table)
        self.play(Write(tex_table),run_time=20)
        self.wait(4)
        wahrheitstafel = Text("Wahrheitstafel")
        wahrheitstafel.to_corner(UP + LEFT)
        self.play(
            FadeOut(tex_table),
            LaggedStart(*[Transform(junktoren, wahrheitstafel)]),
        )
        table = r"""
        \begin{table}[]
        \centering
        \begin{tabular}{|l|l|l|l|l|l|l|}\hline
        $A$ & $B$ & $\neg A$ & $A \wedge B$ & $A \vee B$ & $A \Rightarrow B$ & $A \Leftrightarrow B$ \\
            w   & w   & f        & w            & w          & w                 & w                     \\
            w   & f   & f        & f            & w          & f                 & f                     \\
            f   & w   & w        & f            & w          & w                 & f                     \\
            f   & f   & w        & f            & f          & w                 & w                     \\ \hline
        \end{tabular}
        \end{table}
        """
        tex_table = Tex(table)
        self.play(Write(tex_table),run_time=20)
        self.play(FadeOut(tex_table),FadeOut(junktoren))
        gesetze = Text("Gesetze der Aussagenlogik")
        gesetze1 = Text("Gesetze der Aussagenlogik")
        gesetze1.to_corner(UP + LEFT)
        self.play(Write(gesetze), )
        self.wait(1)
        self.play(Transform(gesetze, gesetze1))
        self.wait(2)

