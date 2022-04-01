from manim import *

class GeometrischeReihe(Scene):
    def construct(self):
        author = Text("Mathetastic",font_size=11, color=PINK)
        author.to_corner(DR)
        course = Text("V1G1 - Analyis 1 - Die geometrische Reihe",font_size=11, color=PINK)
        course.to_corner(DL)
        title = Text("Die geometrische Reihe")
        Sum_Expression = MathTex(r"\sum_{i = 0}^{\infty}x^i", substrings_to_isolate="x")
        Sum_Expression.set_color_by_tex("x", YELLOW)
        VGroup(title, Sum_Expression).arrange(DOWN)
        self.wait(1)
        self.add(course)
        self.add(author)
        self.wait(1)
        self.play(
            Write(title),
            Write(Sum_Expression)
        )
        self.wait(3)

        formel = MathTex(r"&= 1 + x + x^2 + x^3 + x^4 + \ldots", substrings_to_isolate="x")
        formel.set_color_by_tex("x", YELLOW)
        self.play(
            VGroup(Sum_Expression, title).animate.arrange(RIGHT),
            )
        self.play(
            Transform(title, formel)
        )
        formel = title
        self.wait(3)
        self.play(
            VGroup(Sum_Expression, formel).animate.arrange(RIGHT),
            )

        Beispiel= Text("Beispiel 1")
        Beispiel.to_corner(UP + LEFT)
        self.play(
            Write(Beispiel),
        )
        self.wait(3)
        t= MathTex(r"= 1^0+ 1 + 1^2 + 1^3+ \ldots",substrings_to_isolate="1")
        t1= MathTex(r"\sum_{i = 0}^{\infty}1^i",substrings_to_isolate="1")
        t.set_color_by_tex("1", YELLOW)
        t1.set_color_by_tex("1", YELLOW)
        VGroup(t1, t).arrange(RIGHT)
        self.play(    
            Transform(Sum_Expression,t1),   
            Transform(formel, t),
        )
        self.wait(3)
        t2= MathTex(r"\sum_{i = 0}^{\infty}(-1)^i", substrings_to_isolate="-")
        t2.set_color_by_tex("-", YELLOW)
        self.play(Transform(Beispiel, Text("Beispiel 2").to_corner(UP+ LEFT)),
                
        )
        
        VGroup(t2, formel).arrange(RIGHT)
        t3 = MathTex(r"= 1+ (-1)^1 + (-1)^2 + \ldots",substrings_to_isolate="-1")
        t3.set_color_by_tex("-1", YELLOW)
        VGroup(t2, t3).arrange(RIGHT)
        self.play(Transform(Sum_Expression, t2),
            Transform(formel, t3)
        )
        self.wait(3)
        self.play(FadeOut(formel),
        FadeOut(Beispiel),
        FadeOut(Sum_Expression)
        )
        self.wait(2)
        konvergenz = Text("Konvergenz der Reihe")
        self.play(Write(konvergenz))
        self.wait(2)
        self.play(Transform(konvergenz, Tex("Für $|x| < 1$ gilt:").to_corner(UP+LEFT)))
        summe = MathTex(r"\sum_{i=0}^{\infty} x^i =\frac{1}{1-x}")
        self.play(Write(summe))
        self.wait(3)
        sn= MathTex(r"S_n = \sum_{i=0}^n x^i")
        sn.to_corner(UP+RIGHT)
        self.play(Transform(summe, sn))
        self.wait(2)
        latex = MathTex(r'(x-1)\cdot S_n &= x \cdot \sum_{i=0}^n x^i - \sum_{i=0}^n x^i \\ &= \sum_{i=0}^n x\cdot x^i - \sum_{i=0}^n x^i \\ &= \sum_{i=0}^{n} x^{i+1} - \sum_{i=1}^n x^i \\ &= \sum_{i=0}^{n+1} x^i - \sum_{i=0}^n x^i \\ &= x^{i+1} - x^0', font_size=30)
        self.play(AddTextWordByWord(latex, run_time=20.0))
        self.wait(3)
        self.play(FadeOut(latex),FadeOut(summe))
        folgerung= MathTex(r"\sum_{i=0}^n x^i = \frac{1-x^{n+1}}{1-x}")
        self.play(Write(folgerung))

