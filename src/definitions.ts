import { Color } from "./color";

// Colors

const none = new Color("#000000").setAlpha(0);
const white = new Color("#ffffff");
const black = new Color("#000000");
const grey = new Color("#bec9d3", "#2e2e37");
const greyStrong = new Color("#6b7a88", "#a8a8b1");
const greyLight = new Color("#e7ecf2", "#1e1d27");
const greyOnBlack = new Color("#65696e", grey);

const purple = new Color("#7d46fc");
const blue = new Color("#004bff");
const cyan = new Color("#00d2ff");
const green = new Color("#00ff68");
const yellow = new Color("#ffca00");
const orange = new Color("#ff9900");
const red = new Color("#ff0032");

const main = new Color(white, black);
const mainNegative = new Color(black, white);
const mainContrast = new Color("#f4f6fc", "#0a0b0f");
const mainContrastTransparent = new Color("#99a7e1", "#616a93").setAlpha(0.1);

const primary = new Color(blue, purple);
const primaryNegative = white;
const primaryHighlight = new Color("#0064ff", primary).setAlpha(0.15, 0.25);
const primaryHighlightStrong = primaryHighlight.withAlpha(0.3, 0.5);
const primaryHighlightLight = primaryHighlight.withAlpha(0.05, 0.08);

const added = green;
const addedHighlight = added.withAlpha(0.1, 0.2);
const deleted = red;
const deletedHighlight = deleted.withAlpha(0.1, 0.2);

const error = red;
const warning = orange;

const find = yellow.withAlpha(0.6);
const findHighlight = find.withAlpha(0.3);

const border = greyLight;

// Theme settings

export default {
    colors: {
        "activityBar.background": main,
        "activityBar.border": none,
        "activityBar.foreground": grey,
        "activityBarBadge.background": mainNegative,
        "activityBarBadge.foreground": main,
        "badge.background": mainNegative,
        "badge.foreground": main,
        "button.background": primary,
        "button.foreground": primaryNegative,
        "contrastBorder": none,
        "diffEditor.insertedTextBackground": addedHighlight,
        "diffEditor.removedTextBackground": deletedHighlight,
        "dropdown.background": mainContrast,
        "dropdown.border": border,
        "dropdown.foreground": mainNegative,
        "editor.background": main,
        "editor.findMatchBackground": find,
        "editor.findMatchHighlightBackground": findHighlight,
        "editor.foreground": mainNegative,
        "editor.lineHighlightBackground": primaryHighlightLight,
        "editor.lineHighlightBorder": none,
        "editor.selectionBackground": primaryHighlightStrong,
        "editor.selectionForeground": main,
        "editor.wordHighlightBackground": primaryHighlight,
        "editor.wordHighlightStrongBackground": primaryHighlightStrong,
        "editorBracketMatch.background": primaryHighlightStrong,
        "editorBracketMatch.border": none,
        "editorCursor.foreground": primary,
        "editorError.foreground": error,
        "editorGroup.border": mainContrast,
        "editorGroupHeader.tabsBackground": main,
        "editorGroupHeader.tabsBorder": none,
        "editorGutter.addedBackground": added,
        "editorGutter.deletedBackground": deleted,
        "editorGutter.modifiedBackground": mainNegative,
        "editorIndentGuide.background": mainContrast,
        "editorLineNumber.foreground": new Color("#ebf0f5", greyLight),
        "editorLink.activeForeground": primary,
        "editorOverviewRuler.addedForeground": none,
        "editorOverviewRuler.border": none,
        "editorOverviewRuler.bracketMatchForeground": primaryHighlightStrong,
        "editorOverviewRuler.errorForeground": error,
        "editorOverviewRuler.findMatchForeground": find,
        "editorOverviewRuler.modifiedForeground": mainNegative,
        "editorOverviewRuler.selectionHighlightForeground": primaryHighlightStrong,
        "editorOverviewRuler.warningForeground": warning,
        "editorOverviewRuler.wordHighlightForeground": primaryHighlight,
        "editorOverviewRuler.wordHighlightStrongForeground": primaryHighlightStrong,
        "editorRuler.foreground": mainContrast,
        "editorSuggestWidget.foreground": mainNegative,
        "editorWarning.foreground": warning,
        "editorWidget.background": mainContrast,
        "editorWidget.border": border,
        "errorForeground": error,
        "extensionButton.prominentBackground": primary,
        "extensionButton.prominentForeground": primaryNegative,
        "extensionButton.prominentHoverBackground": primary,
        "focusBorder": border,
        "foreground": mainNegative,
        "gitDecoration.ignoredResourceForeground": grey,
        "gitDecoration.modifiedResourceForeground": mainNegative,
        "gitDecoration.untrackedResourceForeground": mainNegative,
        "input.background": mainContrast,
        "input.border": border,
        "input.foreground": mainNegative,
        "input.placeholderForeground": grey,
        "list.activeSelectionBackground": mainNegative,
        "list.activeSelectionForeground": main,
        "list.dropBackground": primaryHighlightStrong,
        "list.focusBackground": primaryHighlight,
        "list.focusForeground": mainNegative,
        "list.highlightForeground": mainNegative,
        "list.hoverBackground": mainContrast,
        "list.inactiveSelectionBackground": mainContrast,
        "list.inactiveSelectionForeground": mainNegative,
        "panel.background": mainContrast,
        "panel.border": none,
        "panelTitle.activeBorder": grey,
        "peekView.border": mainNegative,
        "peekViewEditor.background": none,
        "peekViewEditor.matchHighlightBackground": find,
        "peekViewResult.background": none,
        "peekViewResult.matchHighlightBackground": find,
        "peekViewResult.selectionBackground": mainNegative,
        "peekViewResult.selectionForeground": main,
        "peekViewTitle.background": none,
        "peekViewTitleDescription.foreground": grey,
        "peekViewTitleLabel.foreground": mainNegative,
        "progressBar.background": primary,
        "scrollbar.shadow": none,
        "scrollbarSlider.background": mainContrastTransparent,
        "scrollbarSlider.hoverBackground": mainNegative,
        "sideBar.background": main,
        "sideBar.foreground": greyStrong,
        "sideBarSectionHeader.background": mainContrast,
        "sideBarSectionHeader.foreground": greyStrong,
        "sideBarTitle.foreground": grey,
        "statusBar.background": black,
        "statusBar.foreground": greyOnBlack,
        "statusBar.noFolderBackground": black,
        "tab.activeBackground": mainNegative,
        "tab.activeForeground": main,
        "tab.border": none,
        "tab.inactiveBackground": none,
        "tab.inactiveForeground": grey,
        "terminal.ansiBlack": mainNegative,
        "terminal.ansiBlue": blue,
        "terminal.ansiBrightBlack": mainNegative,
        "terminal.ansiBrightBlue": blue,
        "terminal.ansiBrightCyan": cyan,
        "terminal.ansiBrightGreen": green,
        "terminal.ansiBrightMagenta": purple,
        "terminal.ansiBrightRed": red,
        "terminal.ansiBrightWhite": greyStrong,
        "terminal.ansiBrightYellow": yellow,
        "terminal.ansiCyan": cyan,
        "terminal.ansiGreen": green,
        "terminal.ansiMagenta": purple,
        "terminal.ansiRed": red,
        "terminal.ansiWhite": greyStrong,
        "terminal.ansiYellow": yellow,
        "terminal.foreground": mainNegative,
        "terminal.selectionBackground": primaryHighlightStrong,
        "terminalCursor.foreground": primary,
        "textLink.activeForeground": primary,
        "textLink.foreground": primary,
        "titleBar.activeBackground": main,
        "titleBar.activeForeground": greyStrong,
        "titleBar.inactiveBackground": main,
        "titleBar.inactiveForeground": grey,
        "welcomePage.buttonBackground": mainContrast,
        "welcomePage.buttonHoverBackground": primaryHighlight,
        "widget.shadow": none,
    },
    tokenColors: [
        {
            scope: ["comment", "string.quoted.docstring"],
            settings: {
                foreground: grey,
            },
        },
        {
            scope: ["string"],
            settings: {
                foreground: greyStrong,
            },
        },
        {
            scope: [
                "punctuation.definition.string",
                "storage.type.string.python",
            ],
            settings: {
                foreground: mainNegative,
            },
        },
        {
            scope: [
                "beginning.punctuation",
                "entity.name.section.group-title",
                "entity.name.tag",
                "entity.other.attribute-name.class",
                "entity.other.attribute-name.id",
                "keyword.const",
                "keyword.control",
                "keyword.function",
                "keyword.import",
                "keyword.operator.assignment",
                "keyword.operator.comparison",
                "keyword.operator.decrement",
                "keyword.operator.expression",
                "keyword.operator.increment",
                "keyword.operator.increment-decrement",
                "keyword.operator.logical",
                "keyword.operator.new",
                "keyword.operator.other",
                "keyword.other.special-method",
                "keyword.package",
                "keyword.type",
                "keyword.var",
                "markup.heading",
                "meta.function.decorator",
                "meta.tag.sgml.doctype.html",
                "punctuation.separator.key-value",
                "storage.modifier",
                "storage.type.class",
                "storage.type.enum",
                "storage.type.function",
                "storage.type.import",
                "storage.type.interface",
                "storage.type.js",
                "storage.type.namespace",
                "storage.type.property",
                "storage.type.string.python",
                "storage.type.ts",
            ],
            settings: {
                fontStyle: "bold",
            },
        },
    ],
};
