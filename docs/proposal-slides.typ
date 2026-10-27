#import "@preview/typslides:1.3.4": *

// Project configuration
#show: typslides.with(
  ratio: "16-9",
  theme: "greeny",
  font: "Segoe UI",
  font-size: 20pt,
  link-style: "color",
  show-progress: true,
)

// The front slide is the first slide of your presentation
#front-slide(
  title: "Language Modeling in Jejueo",
  authors: "Zeke Mackay",
)

#slide(title: "Jejueo Language Introduction")[
  #grid(
    columns: (1fr, 1fr),
    gutter: 12pt
    ,
    [
  - Closely related to Korean, minority language in South Korea
  - Little support from Korean government
  - Critically endangered, with 5,000 native speakers
    ]    ,
    [
      #image("img/Jeju_Province_in_South_Korea.svg")
    ]
  )

  
]

#slide(title: "Research Goal")[
  - Create and evaluate generative models of Jejueo text
  - Revitalization benefits of language modeling
    - Aids in education
    - Supports future machine translation
    - Supports linguistic research
]

#slide(title: "Current Progress")[
  - Dataset
    - Jejueo Interview Transcripts
    - 170,000 sentences in Jejueo (with Korean translations)
  - Byte-Pair Encoding implementation
  - N-Gram Model implementation
]

#slide(title: "Future Goals")[
  - Improvements to basic N-Gram models
    - Smoothing 
    - Backoff
    - Interpolation
  - Evaluation
    - Train/Test data split
    - Perplexity metric
]