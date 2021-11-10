from manim import *


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(BLUE, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen


class Rainbow(Scene):
    def construct(self):
        r = Text("RAINBOW", font_size=96)
        r[0].set_color(RED)
        r[1].set_color(ORANGE)
        r[2].set_color(YELLOW)
        r[3].set_color(GREEN)
        r[4].set_color(TEAL)
        r[5].set_color(BLUE)
        r[6].set_color(PURPLE)

        self.play(Write(r), run_time = 4)
        self.play(r.animate.scale(2), run_time = 2)
        self.play(FadeOut(r))

class DeutschsAlgo(Scene):
    def construct(self):
        title = Text("Deutsch's Algorithm", font_size = 80, color = BLUE)
        title.shift(UP*2)
        self.play(
            FadeIn(title)
        )
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage{physics}")

        # Algorithm simplification
        line1 = MathTex(
            r"(\mathbb{H} \otimes I)",
            r"F",
            r"(\mathbb{H} \otimes \mathbb{H})",
            r"(\hat{\vb{e}}_0 \otimes \hat{\vb{e}}_1)",
            tex_template=template,
            font_size = 55)
        line2 = MathTex(
            "=",
            r"(\mathbb{H} \otimes I)",
            r"F",
            r"(\mathbb{H}\hat{\vb{e}}_0 \otimes \mathbb{H}\hat{\vb{e}}_1)",
            tex_template=template,
            font_size = 55)
        line3 = MathTex(
            "=",
            r"(\mathbb{H} \otimes I)",
            r"F",
            r"\frac{1}{2}((\hat{\vb{e}}_0 + \hat{\vb{e}}_1)\otimes (\hat{\vb{e}}_0-\hat{\vb{e}}_1))",
            tex_template=template,
            font_size = 55)
        line4 = MathTex(
            "="
            r"\frac{1}{2}",
            r"(\mathbb{H} \otimes I)",
            r"F",
            r"(\hat{\vb{e}}_{00} - \hat{\vb{e}}_{01} + \hat{\vb{e}}_{10} - \hat{\vb{e}}_{11})",
            tex_template=template,
            font_size = 55)
        line5 = MathTex(
            "="
            r"\frac{1}{2}",
            r"(\mathbb{H} \otimes I)",
            r"(\hat{\vb{e}}_{0f(0)} - \hat{\vb{e}}_{0\neg f(0)} + \hat{\vb{e}}_{1f(1)} - \hat{\vb{e}}_{1\neg f(1)})",
            tex_template=template,
            font_size = 55)

        # Colors
#         line1.set_color_by_gradient(PURE_GREEN, PURE_RED)
#         line2.set_color_by_gradient(PURE_GREEN, PURE_RED)
#         line3.set_color_by_gradient(PURE_GREEN, PURE_RED)
#         line4.set_color_by_gradient(PURE_GREEN, PURE_RED)

        # Animations
        self.play(Write(line1))
        self.wait(3)
        self.play(
            TransformMatchingTex(line1, line2),
        )
        self.wait(3)
        self.play(
            TransformMatchingTex(line2, line3),
        )
        self.wait(3)
        self.play(
            TransformMatchingTex(line3, line4),
        )
        self.wait(3)
        self.play(
            TransformMatchingTex(line4, line5),
        )
        self.wait(3)
