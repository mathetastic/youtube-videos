from manim import *

class GeometrischeReihe(Scene):
    def construct(self):
        author = Text("NicoSky",font_size=11, color=RED)
        author.to_corner(DR)
        course = Text("V1G1 - Analyis 1 - Die geometrische Reihe",font_size=11, color=YELLOW)
        course.to_corner(DL)
        title = Text("Die geometrische Reihe")
        Sum_Expression = MathTex(r"\sum_{i = 0}^{\infty}x^i")
        VGroup(title, Sum_Expression).arrange(DOWN)
        self.wait(1)
        self.play(Write(course))
        self.add(author)
        self.wait(1)
        self.play(
            Write(title),
            Write(Sum_Expression)
        )
        self.wait(3)

        formel = MathTex(r"= 1 + x + x^2 + x^3 + x^4 + x^5 ...")
        self.play(
            VGroup(Sum_Expression, title).animate.arrange(RIGHT),
            )
        self.play(
            Transform(title, formel)
        )
        formel = title
        self.wait(3)

        Behauptung = Text("Behauptung")
        Behauptung.to_corner(UP + LEFT)
        self.play(
            Write(Behauptung),
        )
        self.play(            
            Transform(formel, MathTex(r"= \frac{1}{1-x} \Leftrightarrow |x| < 1")),
        )
        self.play(
            VGroup(Sum_Expression, formel).animate.arrange(RIGHT),
            )
        self.wait(3)

        Beweis = Text("Beweis")
        Beweis.to_corner(UP + LEFT)
        self.play(
            Transform(Behauptung, Beweis)
        )
        Beweis = Behauptung
        self.play(
            Transform(VGroup(Sum_Expression,formel).arrange(RIGHT),VGroup(MathTex(r"\sum_{i = 0}^{n}x^i"),MathTex(r"= \sum_{i = 0}^{n}x^i")).arrange(RIGHT))
        )
        self.wait(1)
        self.play(
            Transform(VGroup(Sum_Expression,formel).arrange(RIGHT),VGroup(MathTex(r"(1 - x)\sum_{i = 0}^{n}x^i"),MathTex(r"= (1 - x)\sum_{i = 0}^{n}x^i")).arrange(RIGHT))
        )
        self.wait(1)
        self.play(
            Transform(VGroup(Sum_Expression,formel).arrange(RIGHT),VGroup(Sum_Expression,MathTex(r"= \sum_{i = 0}^{n}x^i - \sum_{i = 1}^{n + 1}x^i")).arrange(RIGHT))
        )
        self.wait(1)
        self.play(
            Transform(VGroup(Sum_Expression,formel).arrange(RIGHT),VGroup(Sum_Expression,MathTex(r"= 1 - x^n")).arrange(RIGHT))
        )
        self.wait(1)
        self.play(
            Transform(VGroup(Sum_Expression,formel).arrange(RIGHT),VGroup(MathTex(r"\sum_{i = 0}^{n}x^i"),MathTex(r"= \frac{1-x^n}{1-x}")).arrange(RIGHT))
        )
        self.wait(1)
        self.play(
            Transform(VGroup(Sum_Expression,formel).arrange(RIGHT),VGroup(MathTex(r"\lim_{n \to \infty} \sum_{i = 0}^{n}x^i"),MathTex(r"= \lim_{n \to \infty} \frac{1 - x^n}{1 - x}")).arrange(RIGHT))
        )
        self.wait(1)
        self.play(
            Transform(VGroup(Sum_Expression,formel).arrange(RIGHT),VGroup(MathTex(r"\sum_{i = 0}^{\infty}x^i"),MathTex(r"=  \frac{1 - \displaystyle\lim_{n \to \infty} x^n}{1 - x}")).arrange(RIGHT))
        )
        self.wait(1)
        self.play(
            Transform(VGroup(Sum_Expression,formel).arrange(RIGHT),VGroup(Sum_Expression,MathTex(r"=  \frac{1 - 0}{1 - x}\Leftrightarrow |x| < 1")).arrange(RIGHT))
        )
        self.wait(1)
        gr = VGroup(Sum_Expression,MathTex(r"=  \frac{1}{1 - x}\Leftrightarrow |x| < 1")).arrange(RIGHT)
        self.play(
            Transform(VGroup(Sum_Expression,formel).arrange(RIGHT),gr)
        )
        QED = Text("QED")
        QED.next_to(gr,RIGHT)
        self.play(
            Write(QED)
        )
        self.wait(5)