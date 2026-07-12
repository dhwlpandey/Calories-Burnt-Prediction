---
name: Kinetic Analytics
colors:
  surface: '#f8f9ff'
  surface-dim: '#cbdbf5'
  surface-bright: '#f8f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eff4ff'
  surface-container: '#e5eeff'
  surface-container-high: '#dce9ff'
  surface-container-highest: '#d3e4fe'
  on-surface: '#0b1c30'
  on-surface-variant: '#424754'
  inverse-surface: '#213145'
  inverse-on-surface: '#eaf1ff'
  outline: '#727785'
  outline-variant: '#c2c6d6'
  surface-tint: '#005ac2'
  primary: '#0058be'
  on-primary: '#ffffff'
  primary-container: '#2170e4'
  on-primary-container: '#fefcff'
  inverse-primary: '#adc6ff'
  secondary: '#006c49'
  on-secondary: '#ffffff'
  secondary-container: '#6cf8bb'
  on-secondary-container: '#00714d'
  tertiary: '#994100'
  on-tertiary: '#ffffff'
  tertiary-container: '#c05400'
  on-tertiary-container: '#fffbff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d8e2ff'
  primary-fixed-dim: '#adc6ff'
  on-primary-fixed: '#001a42'
  on-primary-fixed-variant: '#004395'
  secondary-fixed: '#6ffbbe'
  secondary-fixed-dim: '#4edea3'
  on-secondary-fixed: '#002113'
  on-secondary-fixed-variant: '#005236'
  tertiary-fixed: '#ffdbca'
  tertiary-fixed-dim: '#ffb690'
  on-tertiary-fixed: '#341100'
  on-tertiary-fixed-variant: '#783200'
  background: '#f8f9ff'
  on-background: '#0b1c30'
  surface-variant: '#d3e4fe'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-lg-mobile:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: 0.01em
  mono-sm:
    fontFamily: JetBrains Mono
    fontSize: 13px
    fontWeight: '400'
    lineHeight: 18px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  container-padding: 24px
  gutter: 16px
  card-gap: 24px
  section-margin: 48px
---

## Brand & Style

The design system is engineered for an academic yet professional Machine Learning environment focused on health and fitness. The personality is "Intellectual Vitality"—balancing the rigorous, data-driven nature of predictive modeling with the active, energetic essence of physical health.

The style is **Modern Corporate** with a **Glassmorphic** twist. It utilizes expansive whitespace and a structured grid to maintain an organized, research-grade appearance. To prevent the UI from feeling sterile, soft gradients and translucent glass layers are used on secondary surfaces to inject a sense of modern "tech-forward" energy. The emotional response should be one of confidence, clarity, and motivation.

## Colors

This design system uses a logic-based palette where color signifies specific data states:
- **Primary (Soft Blue):** Used for the core "Technology" layer—buttons, active states, and prediction primary actions.
- **Success (Fresh Green):** Reserved for health achievements, positive growth metrics, and "Model Ready" indicators.
- **Accent (Energetic Orange):** Specifically mapped to caloric data, metabolic heat, and energy expenditure metrics.
- **Background & Surfaces:** A base of Pure White (#FFFFFF) sits atop a soft blue-grey foundation (#F8FAFC) to create a subtle distinction between the canvas and the application surface.
- **Gradients:** Use linear gradients (135°) from the base color to a 20% lighter tint for primary action cards and header highlights.

## Typography

The typography system relies on **Inter** for its neutral, highly legible, and systematic qualities. It emphasizes a clear hierarchy to help users distinguish between model inputs, prediction outputs, and academic citations.

- **Display & Headlines:** Use tight letter spacing and bold weights to ground the data.
- **Body:** Standard weight with generous line height for readability of research summaries.
- **Monospace:** For technical data points, model parameters (e.g., RMSE, R²), or feature names, use JetBrains Mono to reinforce the "student-developed tool" aesthetic.

## Layout & Spacing

The layout follows a **Fluid Grid** system within a max-width container of 1280px for desktop. 

- **Grid:** 12-column layout for desktop, 8-column for tablet, and 4-column for mobile.
- **Rhythm:** An 8px base unit governs all dimensions.
- **Density:** Use "Comfortable" spacing for the input dashboard to reduce cognitive load, while switching to "Compact" for data tables and feature importance charts.
- **Adaptation:** On mobile, sidebars reflow to bottom sheets, and the main prediction result card remains pinned to the top of the scroll view.

## Elevation & Depth

This design system uses a tiered elevation model to separate the "Analytical" layer from the "Interactive" layer:

1.  **Level 0 (Floor):** The #F8FAFC background.
2.  **Level 1 (Cards):** Pure White cards with a very soft, diffused shadow (`box-shadow: 0 4px 20px rgba(148, 163, 184, 0.1)`).
3.  **Level 2 (Interaction):** Hovered cards lift slightly with a more pronounced shadow and a 1px border colored by the primary blue at 20% opacity.
4.  **Glassmorphism (Overlays):** Used for modal backgrounds or "Model Processing" states. Apply a background blur of 12px and a white-transparent fill (rgba(255, 255, 255, 0.7)) with a subtle 1px white inner-border.

## Shapes

The design system utilizes a **Rounded** shape language to appear approachable and modern. 

- **Base Radius:** 16px (rounded-xl) for all main containers and cards to create a friendly, high-end feel.
- **Internal Elements:** Buttons and input fields use 8px (rounded-lg) to maintain a slightly more structured look inside the larger containers.
- **Interactive States:** Hovering over a card should trigger a subtle `scale(1.02)` transform alongside shadow deepening.

## Components

- **Buttons:** Primary buttons use a solid Soft Blue fill with white text. Secondary buttons use a ghost style (blue border, no fill). Energy-related actions use the Orange gradient.
- **Inputs:** Text fields and sliders should feel tactile. Sliders use the Primary Blue for the track and a white thumb with a heavy shadow.
- **Cards:** Data cards are the primary vessel. Every card should have a 16px corner radius and a subtle 1px border (`#E2E8F0`).
- **Chips/Labels:** Use for feature categories (e.g., "Demographic", "Activity"). Small, 4px rounded corners, using low-opacity versions of the primary/secondary colors.
- **Prediction Display:** A large, glassmorphic card for the final calorie count, using a bold Display font and the Energetic Orange for the value.
- **Charts:** Use thin lines, no background fill (or very light gradient fill), and circular data points.