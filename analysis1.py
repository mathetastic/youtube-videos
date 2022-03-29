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
        self.play(FadeOut(junktoren))

        table = r"""        

        "A impliziert B" & $A \implies B$ & \emph{Implikation} \\
        "A gdw. B" & $A \iff B$ & \emph{Äquivalenz}    \\\hline
        \end{tabular}
        \end{table}
        """
        #tex_table = Tex(table)
        #self.add(tex_table)
        t2 = (r"\neg A")
        t1 = (r"\text{nicht A}")
        t3 = (r"\text{Negation}")
        t4 = (r"\text{A und B}")
        t5= (r"A \wedge B")
        t6 = (r"\text{Konjunktion}")
        t7 = (r"\text{A oder B}")
        t8 = (r"A \vee B")
        t9 = (r"\text{Disjunktion}")
        t10 = (r"\text{A impliziert B")
        t11= (r"A \iff B")
        t12= (r"\text{Implikation}")
        t13 = (r"\text{A gdw. B}")
        t14= (r"A \iff B")
        t15 = (r"\text{Äquivalenz}")
    
        table = MathTable(
            [[t1,t2,t3],
            [t4,t5,t6],[t7,t8,t9],[t10,t11,t12],[t13,t14,t15]],
            col_labels=[Text("Gesprochen", font_size=22), Text("Symbol",font_size=22), Text("Name",font_size=22)])
        table.add(SurroundingRectangle(table.get_rows()[1]).set_color(GREEN))
        self.add(table)
        table1 = MathTable(
            [[t1,t2,t3],
            [t4,t5,t6],[t7,t8,t9],[t10,t11,t12],[t13,t14,t15]],
            col_labels=[Text("Gesprochen", font_size=22), Text("Symbol",font_size=22), Text("Name",font_size=22)])
        self.add(table1)
        self.wait(4)
        self.play(FadeOut(table))
        table1.add(SurroundingRectangle(table.get_rows()[2]).set_color(GREEN))
        table2 = MathTable(
            [[t1,t2,t3],
            [t4,t5,t6],[t7,t8,t9],[t10,t11,t12],[t13,t14,t15]],
            col_labels=[Text("Gesprochen", font_size=22), Text("Symbol",font_size=22), Text("Name",font_size=22)])
        self.add(table2)
        self.wait(4)
        self.play(FadeOut(table1))
        table2.add(SurroundingRectangle(table.get_rows()[3]).set_color(GREEN))
        table3 = MathTable(
            [[t1,t2,t3],
            [t4,t5,t6],[t7,t8,t9],[t10,t11,t12],[t13,t14,t15]],
            col_labels=[Text("Gesprochen", font_size=22), Text("Symbol",font_size=22), Text("Name",font_size=22)])
        self.add(table3)
        self.wait(4)
        self.play(FadeOut(table2))
        table3.add(SurroundingRectangle(table.get_rows()[4]).set_color(GREEN))
        table4 = MathTable(
            [[t1,t2,t3],
            [t4,t5,t6],[t7,t8,t9],[t10,t11,t12],[t13,t14,t15]],
            col_labels=[Text("Gesprochen", font_size=22), Text("Symbol",font_size=22), Text("Name",font_size=22)])
        self.add(table4)
        self.wait(4)
        self.play(FadeOut(table3))
        table4.add(SurroundingRectangle(table.get_rows()[5]).set_color(GREEN))
        
    
        
        self.wait(4)
        wahrheitstafel = Text("Wahrheitstafel")
        wahrheitstafel.to_corner(UP + LEFT)
        self.play(
            LaggedStart(*[Transform(table4, wahrheitstafel)]),
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
        self.add(tex_table)
        self.play(FadeOut(tex_table),FadeOut(table4))
        gesetze = Text("Gesetze der Aussagenlogik")
        gesetze1 = Text("Gesetze der Aussagenlogik")
        gesetze1.to_corner(UP + LEFT)
        self.play(Write(gesetze), )
        self.wait(1)
        self.play(Transform(gesetze, gesetze1))
        self.wait(2)

