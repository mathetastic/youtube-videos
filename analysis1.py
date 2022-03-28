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

        transform_title = Text("Ausage")
        transform_title.to_corner(UP + LEFT)
        self.play(
            Transform(title, transform_title),
            LaggedStart(*[FadeOut(obj, shift=DOWN) for obj in basel]),
        )
        aussage = Text("- mathematischer oder sprachlicher Satz \n- wahr oder falsch")
        beispiel = Text("Beispiele")
        beispiel.to_corner(UP+ LEFT)
        self.play(Write(aussage),)
        self.wait(4)
        self.play(
            LaggedStart(*[FadeOut(obj, shift=DOWN) for obj in aussage]),
            Transform(title, beispiel),
        )
        
