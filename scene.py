from manim import *

class DeutschsAlgo(Scene):
    def construct(self):
        title = Text("Deutsch's Algorithm", font_size = 80, color = BLUE)
        title.shift(UP*2)
        self.play(
            FadeIn(title)
        )
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage{physics}")

        special_matrices = Text("Tools: ", font_size = 30, color = ORANGE)

        H = MathTex(
            r"\mathbb{H} =",
            r"\frac{1}{\sqrt{2}}",
            r"\mqty(1 & 1 \\ 1 & -1)",
            tex_template=template,
            font_size = 30
        ).next_to(special_matrices, RIGHT)

        X = MathTex(
            r"X =",
            r"\mqty(0 & 1 \\ 1 & 0)",
            tex_template=template,
            font_size = 30
        ).next_to(H, RIGHT)

        I = MathTex(
            r"I =",
            r"\mqty(1 & 0 \\ 0 & 1)",
            tex_template=template,
            font_size = 30
        ).next_to(X, RIGHT)

        e_0 = MathTex(
            r"\hat{\vb{e}}_0",
            "=",
            r"\mqty(1 \\ 0)",
            tex_template=template,
            font_size = 30
        ).next_to(I, RIGHT)

        e_1 = MathTex(
            r"\hat{\vb{e}}_0",
            "=",
            r"\mqty(0 \\ 1)",
            tex_template=template,
            font_size = 30
        ).next_to(e_0, RIGHT)

        matrix_group = VGroup()
        matrix_group.add(special_matrices)
        matrix_group.add(H)
        matrix_group.add(X)
        matrix_group.add(I)
        matrix_group.add(e_0)
        matrix_group.add(e_1)
        center = Point(location = [0., 0., 0.])
        matrix_group.move_to(center)

        # Algorithm simplification
        line0 = MathTex(
            r"(\mathbb{H} \otimes I)",
            r"F",
            r"(\mathbb{H} \otimes \mathbb{H})",
            r"(I \otimes X)",
            r"(\hat{\vb{e}}_0 \otimes \hat{\vb{e}}_0)",
            tex_template=template,
            font_size = 55
        )
        line1 = MathTex(
            "=",
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
        self.play(FadeIn(matrix_group))
        self.wait(4)
        self.play(
            matrix_group.animate.shift(UP*1).scale(0.6)
        )

        self.play(Write(line0))
        self.wait(3)
        self.play(
            TransformMatchingTex(line0, line1),
        )
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
