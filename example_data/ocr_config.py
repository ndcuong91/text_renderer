import os
from pathlib import Path

from text_renderer.effect import *
from text_renderer.corpus import *
from text_renderer.config import (
    RenderCfg,
    NormPerspectiveTransformCfg,
    GeneratorCfg,
    WhiteTextColorCfg,
)
from text_renderer.effect.curve import Curve
from text_renderer.layout.same_line import SameLineLayout
from text_renderer.layout.extra_text_line import ExtraTextLineLayout


CURRENT_DIR = Path(os.path.abspath(os.path.dirname(__file__)))
OUT_DIR = CURRENT_DIR / "output"
DATA_DIR = CURRENT_DIR
BG_DIR = DATA_DIR / "bg"
BLACK_BG_DIR = DATA_DIR / "black_bg"
CHAR_DIR = DATA_DIR / "char"
FONT_DIR = DATA_DIR / "font"
FONT_LIST_DIR = DATA_DIR / "font_list"
TEXT_DIR = DATA_DIR / "text"

font_cfg = dict(
    font_dir=FONT_DIR,
    font_size=(29, 33),
)

small_font_cfg = dict(
    font_dir=CURRENT_DIR / "font",
    font_size=(26, 28),
)

large_font_cfg = dict(
    font_dir=CURRENT_DIR / "font",
    font_size=(26, 28),
)

perspective_transform = NormPerspectiveTransformCfg(10, 10, 1)
effects = Effects(OneOf([DropoutRand(p=1, dropout_p=(0.1, 0.3)),\
    DropoutHorizontal(p=0.5, num_line=1, thickness=1),
    DropoutVertical(p=0.5, num_line=2,thickness=1),
    Padding(p=1, w_ratio=[0.2, 0.21], h_ratio=[0.7, 0.71], center=True),
    Curve(p=1, period=180, amplitude=(4, 5)),
    #Line(0.3)
    ]))

'''
normal_data1 = GeneratorCfg(
    num_image=300000,
    save_dir=OUT_DIR / "normal_data1",
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        perspective_transform=perspective_transform,
        corpus=WordCorpus(
            WordCorpusCfg(
                text_paths=[TEXT_DIR / "corpus-title.txt"],
                num_word=(2,5),
                filter_by_chars=True,
                chars_file=CHAR_DIR / "dict.txt",
                char_spacing = -0.1,
                **font_cfg
            ),
        ),
        corpus_effects=effects,
    ),
)

normal_data2 = GeneratorCfg(
    num_image=300000,
    save_dir=OUT_DIR / "normal_data2",
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        perspective_transform=perspective_transform,
        corpus=WordCorpus(
            WordCorpusCfg(
                text_paths=[TEXT_DIR / "corpus-title.txt"],
                num_word=(2,5),
                filter_by_chars=True,
                chars_file=CHAR_DIR / "dict.txt",
                **font_cfg
            ),
        ),
        corpus_effects=effects,
    ),
)

normal_data3 = GeneratorCfg(
    num_image=300000,
    save_dir=OUT_DIR / "normal_data3",
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        perspective_transform=perspective_transform,
        corpus=WordCorpus(
            WordCorpusCfg(
                text_paths=[TEXT_DIR / "corpus-title.txt"],
                num_word=(2,5),
                filter_by_chars=True,
                chars_file=CHAR_DIR / "dict.txt",
                char_spacing = 0.1,
                **font_cfg
            ),
        ),
        corpus_effects=effects,
    ),
)

color_data1 = GeneratorCfg(
    num_image=300000,
    save_dir=OUT_DIR / "color_data1",
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        perspective_transform=perspective_transform,
        corpus=WordCorpus(
            WordCorpusCfg(
                text_paths=[TEXT_DIR / "corpus-title.txt"],
                num_word=(2,5),
                filter_by_chars=True,
                chars_file=CHAR_DIR / "dict.txt",
                char_spacing = -0.1,
                **font_cfg
            ),
        ),
        corpus_effects=effects,
        gray = False,
    ),
)

color_data2 = GeneratorCfg(
    num_image=300000,
    save_dir=OUT_DIR / "color_data2",
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        perspective_transform=perspective_transform,
        corpus=WordCorpus(
            WordCorpusCfg(
                text_paths=[TEXT_DIR / "corpus-title.txt"],
                num_word=(2,5),
                filter_by_chars=True,
                chars_file=CHAR_DIR / "dict.txt",
                **font_cfg
            ),
        ),
        corpus_effects=effects,
        gray = False,
    ),
)

color_data3 = GeneratorCfg(
    num_image=300000,
    save_dir=OUT_DIR / "color_data3",
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        perspective_transform=perspective_transform,
        corpus=WordCorpus(
            WordCorpusCfg(
                text_paths=[TEXT_DIR / "corpus-title.txt"],
                num_word=(2,5),
                filter_by_chars=True,
                chars_file=CHAR_DIR / "dict.txt",
                char_spacing = 0.1,
                **font_cfg
            ),
        ),
        corpus_effects=effects,
        gray = False,
    ),
)

white_data = GeneratorCfg(
    num_image=300000,
    save_dir=OUT_DIR / "white_data",
    render_cfg=RenderCfg(
        bg_dir=BLACK_BG_DIR,
        perspective_transform=perspective_transform,
        corpus=WordCorpus(
            WordCorpusCfg(
                text_paths=[TEXT_DIR / "corpus-title.txt"],
                num_word=(2,5),
                filter_by_chars=True,
                chars_file=CHAR_DIR / "dict.txt",
                text_color_cfg=WhiteTextColorCfg(),
                **font_cfg
            ),
        ),
        corpus_effects=effects,
    ),
)
'''
up_normal_data1 = GeneratorCfg(
    num_image=200000,
    save_dir=OUT_DIR / "up_normal_data1",
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        perspective_transform=perspective_transform,
        corpus=WordCorpus(
            WordCorpusCfg(
                text_paths=[TEXT_DIR / "corpus-title_upper.txt"],
                num_word=(2,5),
                filter_by_chars=True,
                chars_file=CHAR_DIR / "dict.txt",
                char_spacing = -0.1,
                **font_cfg
            ),
        ),
        corpus_effects=effects,
    ),
)

up_normal_data2 = GeneratorCfg(
    num_image=200000,
    save_dir=OUT_DIR / "up_normal_data2",
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        perspective_transform=perspective_transform,
        corpus=WordCorpus(
            WordCorpusCfg(
                text_paths=[TEXT_DIR / "corpus-title_upper.txt"],
                num_word=(2,5),
                filter_by_chars=True,
                chars_file=CHAR_DIR / "dict.txt",
                **font_cfg
            ),
        ),
        corpus_effects=effects,
    ),
)

up_normal_data3 = GeneratorCfg(
    num_image=200000,
    save_dir=OUT_DIR / "up_normal_data3",
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        perspective_transform=perspective_transform,
        corpus=WordCorpus(
            WordCorpusCfg(
                text_paths=[TEXT_DIR / "corpus-title_upper.txt"],
                num_word=(2,5),
                filter_by_chars=True,
                chars_file=CHAR_DIR / "dict.txt",
                char_spacing = 0.1,
                **font_cfg
            ),
        ),
        corpus_effects=effects,
    ),
)

up_color_data1 = GeneratorCfg(
    num_image=200000,
    save_dir=OUT_DIR / "up_color_data1",
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        perspective_transform=perspective_transform,
        corpus=WordCorpus(
            WordCorpusCfg(
                text_paths=[TEXT_DIR / "corpus-title_upper.txt"],
                num_word=(2,5),
                filter_by_chars=True,
                chars_file=CHAR_DIR / "dict.txt",
                char_spacing = -0.1,
                **font_cfg
            ),
        ),
        corpus_effects=effects,
        gray = False,
    ),
)

up_color_data2 = GeneratorCfg(
    num_image=200000,
    save_dir=OUT_DIR / "up_color_data2",
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        perspective_transform=perspective_transform,
        corpus=WordCorpus(
            WordCorpusCfg(
                text_paths=[TEXT_DIR / "corpus-title_upper.txt"],
                num_word=(2,5),
                filter_by_chars=True,
                chars_file=CHAR_DIR / "dict.txt",
                **font_cfg
            ),
        ),
        corpus_effects=effects,
        gray = False,
    ),
)

up_color_data3 = GeneratorCfg(
    num_image=200000,
    save_dir=OUT_DIR / "up_color_data3",
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        perspective_transform=perspective_transform,
        corpus=WordCorpus(
            WordCorpusCfg(
                text_paths=[TEXT_DIR / "corpus-title_upper.txt"],
                num_word=(2,5),
                filter_by_chars=True,
                chars_file=CHAR_DIR / "dict.txt",
                char_spacing = 0.1,
                **font_cfg
            ),
        ),
        corpus_effects=effects,
        gray = False,
    ),
)

up_white_data = GeneratorCfg(
    num_image=200000,
    save_dir=OUT_DIR / "up_white_data",
    render_cfg=RenderCfg(
        bg_dir=BLACK_BG_DIR,
        perspective_transform=perspective_transform,
        corpus=WordCorpus(
            WordCorpusCfg(
                text_paths=[TEXT_DIR / "corpus-title_upper.txt"],
                num_word=(2,5),
                filter_by_chars=True,
                chars_file=CHAR_DIR / "dict.txt",
                text_color_cfg=WhiteTextColorCfg(),
                **font_cfg
            ),
        ),
        corpus_effects=effects,
    ),
)


same_line_layout_different_font_size = GeneratorCfg(
    num_image=200000,
    save_dir=OUT_DIR / "same_line",
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        perspective_transform=perspective_transform,
        layout = SameLineLayout(h_spacing=(0.9, 0.91)),
        corpus=[
            WordCorpusSameLine(
                WordCorpusCfg(
                    text_paths=[TEXT_DIR / "corpus-title_upper.txt"],
                    filter_by_chars=True,
                    num_word=(1,3),
                    chars_file=CHAR_DIR / "dict.txt",
                    **large_font_cfg
                ),
            ),
            WordCorpus(
                WordCorpusCfg(
                    text_paths=[TEXT_DIR / "corpus-title.txt"],
                    filter_by_chars=True,
                    num_word=(1,3),
                    chars_file=CHAR_DIR / "dict.txt",
                    **small_font_cfg
                ),
            ),
        ],
        corpus_effects=[effects,effects]
    ),
)


# fmt: off
# The configuration file must have a configs variable
configs = [
    # normal_data1,
    # normal_data2,
    # normal_data3,
    # color_data1,
    # color_data2,
    # color_data3,
    # white_data,
    # up_normal_data1,
    # up_normal_data2,
    # up_normal_data3,
    # up_color_data1,
    # up_color_data2,
    # up_color_data3,
    # up_white_data,
    same_line_layout_different_font_size,

]
# fmt: on
