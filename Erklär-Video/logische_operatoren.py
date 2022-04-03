from manim import *


class Junktoren(Scene):
    def construct(self):
        author = Text("Mathetastic",font_size=11, color=PINK)
        author.to_corner(DR)
        course = Text("Grundlagen",font_size=11, color=PINK)
        course.to_corner(DL)
        self.add(course, author)
        title = Text("Logische Operatoren")
        basel = Text("Verknüpfungen von Ausssagen", font_size=24)
        VGroup(title, basel).arrange(DOWN)
        self.wait(1)
        self.play(Write(title),)
        self.wait(4)
        self.play(FadeIn(basel, shift=DOWN),)
        self.wait(3)
        transform_title = Text("Junktoren")
        transform_title.to_corner(UP + LEFT)
        self.play(
            Transform(title, transform_title),
            LaggedStart(*[FadeOut(obj, shift=DOWN) for obj in basel]),
        )
        self.play(FadeOut(title))
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
        t11= (r"A \implies B")
        t12= (r"\text{Implikation}")
        t13 = (r"\text{A gdw. B}")
        t14= (r"A \iff B")
        t15 = (r"\text{Äquivalenz}")
    
        table = MathTable(
            [[t1,t2,t3],
            [t4,t5,t6],[t7,t8,t9],[t10,t11,t12],[t13,t14,t15]],
            col_labels=[Text("Gesprochen", font_size=22), Text("Symbol",font_size=22), Text("Name",font_size=22)])
        table.add(SurroundingRectangle(table.get_rows()[1]).set_color(GREEN))
        self.play(table.create())
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
        self.wait(3)
        wahrheitstafel = Text("Wahrheitstafel")
        wahrheitstafel.to_corner(UP + LEFT)
        self.play(
            LaggedStart(*[Transform(table4, wahrheitstafel)]),
        )
        self.wait(2)
        self.play(FadeOut(table4))
        self.wait(2)

        a= MathTex(r"A")
        b= MathTex(r"B")
        na= MathTex(r"\neg A")
        k= MathTex(r"A \wedge B")
        d= MathTex(r"A \vee B")
        i = MathTex(r"A \implies B")
        g= MathTex(r"A \iff B")
        w= (r"w")
        f=(r"f")
        table_w = MathTable(
           [[w,w,f,w,w,w,w],[w,f,f,w,f,f,f],[f,w,w,w,f,w,f],[f,f,w,f,f,w,w]],
            col_labels=[ a,b, na, k, d,i,g])
        table_w.scale(0.8)
        table_w.add(SurroundingRectangle(table_w.get_columns()[2]).set_color(GREEN))
        self.play(Write(table_w),run_time=1.5)
        self.wait(3)
        a= MathTex(r"A")
        b= MathTex(r"B")
        na= MathTex(r"\neg A")
        k= MathTex(r"A \wedge B")
        d= MathTex(r"A \vee B")
        i = MathTex(r"A \implies B")
        g= MathTex(r"A \iff B")
        w= (r"w")
        f=(r"f")
        table_w2 = MathTable(
           [[w,w,f,w,w,w,w],[w,f,f,w,f,f,f],[f,w,w,w,f,w,f],[f,f,w,f,f,w,w]],
            col_labels=[a,b, na, k, d,i,g])
        table_w2.scale(0.8)
        self.add(table_w2)
        self.play(FadeOut(table_w))
        table_w2.add(SurroundingRectangle(table_w2.get_columns()[3]).set_color(GREEN))
        self.wait(3)
        a= MathTex(r"A")
        b= MathTex(r"B")
        na= MathTex(r"\neg A")
        k= MathTex(r"A \wedge B")
        d= MathTex(r"A \vee B")
        i = MathTex(r"A \implies B")
        g= MathTex(r"A \iff B")
        w= (r"w")
        f=(r"f")
        table_w3 = MathTable(
           [[w,w,f,w,w,w,w],[w,f,f,w,f,f,f],[f,w,w,w,f,w,f],[f,f,w,f,f,w,w]],
            col_labels=[a,b, na, k, d,i,g])
        table_w3.scale(0.8)
        self.add(table_w3)
        self.play(FadeOut(table_w2))
        table_w3.add(SurroundingRectangle(table_w3.get_columns()[4]).set_color(GREEN))
        self.wait(3)
        a= MathTex(r"A")
        b= MathTex(r"B")
        na= MathTex(r"\neg A")
        k= MathTex(r"A \wedge B")
        d= MathTex(r"A \vee B")
        i = MathTex(r"A \implies B")
        g= MathTex(r"A \iff B")
        w= (r"w")
        f=(r"f")
        table_w4 = MathTable(
           [[w,w,f,w,w,w,w],[w,f,f,w,f,f,f],[f,w,w,w,f,w,f],[f,f,w,f,f,w,w]],
            col_labels=[a,b, na, k, d,i,g])
        table_w4.scale(0.8)
        self.add(table_w4)
        self.play(FadeOut(table_w3))
        table_w4.add(SurroundingRectangle(table_w4.get_columns()[5]).set_color(GREEN))
        self.wait(3)
        a= MathTex(r"A")
        b= MathTex(r"B")
        na= MathTex(r"\neg A")
        k= MathTex(r"A \wedge B")
        d= MathTex(r"A \vee B")
        i = MathTex(r"A \implies B")
        g= MathTex(r"A \iff B")
        w= (r"w")
        f=(r"f")
        table_w5 = MathTable(
           [[w,w,f,w,w,w,w],[w,f,f,w,f,f,f],[f,w,w,w,f,w,f],[f,f,w,f,f,w,w]],
            col_labels=[a,b, na, k, d,i,g])
        table_w5.scale(0.8)
        self.add(table_w5)
        self.play(FadeOut(table_w4))
        table_w5.add(SurroundingRectangle(table_w5.get_columns()[6]).set_color(GREEN))
        self.wait(3)