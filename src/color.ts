import * as tinycolor from "tinycolor2";

export class Color {
    public color: string;
    public alpha: number;
    public nightColor: string;
    public nightAlpha: number;

    /**
     * Get the #rrggbbaa representation of the color.
     *
     * @returns string The color string.
     */
    get hex() {
        return tinycolor(this.color)
            .setAlpha(this.alpha)
            .toHex8String();
    }

    /**
     * Get the #rrggbbaa representation of the night variant of color.
     *
     * @returns string The color string.
     */
    get nightHex() {
        return tinycolor(this.nightColor)
            .setAlpha(this.nightAlpha)
            .toHex8String();
    }

    constructor(color: string | Color, nightColor?: string | Color) {
        if (color instanceof Color) {
            this.color = color.color;
            this.alpha = color.alpha;
            this.nightColor = color.nightColor;
            this.nightAlpha = color.nightAlpha;
        } else {
            this.color = this.nightColor = color;
            this.alpha = this.nightAlpha = 1;
        }

        if (nightColor instanceof Color) {
            this.nightColor = nightColor.nightColor;
            this.nightAlpha = nightColor.nightAlpha;
        } else if (typeof nightColor === "string") {
            this.nightColor = nightColor;
        }
    }

    /**
     * Set alpha for color.
     */
    public setAlpha(alpha: number, nightAlpha?: number): this {
        this.alpha = alpha;
        this.nightAlpha = nightAlpha !== undefined ? nightAlpha : alpha;
        return this;
    }

    /**
     * Get a copy of Color with alpha settings.
     *
     * @returns Color The new Color.
     */
    public withAlpha(alpha: number, nightAlpha?: number): Color {
        const copy = new Color(this.color, this.nightColor);
        copy.setAlpha(alpha, nightAlpha);
        return copy;
    }
}
