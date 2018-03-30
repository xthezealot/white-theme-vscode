"""Themes color definitions."""

from build import ColorSplit


# Colors

colorNone = ColorSplit('#000000').set_alpha(0)
colorWhite = ColorSplit('#ffffff')
colorBlack = ColorSplit('#000000')
colorGrey = ColorSplit('#bec9d3', '#2e2e37')
colorGreyStrong = ColorSplit('#6b7a88', '#a8a8b1')
colorGreyLight = ColorSplit('#e7ecf2', '#1e1d27')
colorGreyOnBlack = ColorSplit('#65696e', colorGrey)

colorPurple = ColorSplit('#7d46fc')
colorBlue = ColorSplit('#004bff')
colorCyan = ColorSplit('#00d2ff')
colorGreen = ColorSplit('#00ff68')
colorYellow = ColorSplit('#ffca00')
colorOrange = ColorSplit('#ff9900')
colorRed = ColorSplit('#ff0032')

colorMain = ColorSplit(colorWhite, colorBlack)
colorMainNegative = ColorSplit(colorBlack, colorWhite)
colorMainContrast = ColorSplit('#f4f6fc', '#0a0b0f')
colorMainContrastTransparent = ColorSplit('#99a7e1', '#616a93').set_alpha(0.1)

colorPrimary = ColorSplit(colorBlue, colorPurple)
colorPrimaryNegative = colorWhite
colorPrimaryHighlight = ColorSplit(
    '#0064ff', colorPrimary).set_alpha(0.15, 0.25)
colorPrimaryHighlightStrong = colorPrimaryHighlight.with_alpha(0.3, 0.5)
colorPrimaryHighlightLight = colorPrimaryHighlight.with_alpha(0.05, 0.08)

colorAdded = colorGreen
colorAddedHighlight = colorAdded.with_alpha(0.1, 0.2)
colorDeleted = colorRed
colorDeletedHighlight = colorDeleted.with_alpha(0.1, 0.2)

colorError = colorRed
colorWarning = colorOrange

colorFind = colorYellow.with_alpha(0.6)
colorFindHighlight = colorFind.with_alpha(0.3)

colorBorder = colorGreyLight


# Theme definitions

definitions = {
    'colors': {
        'activityBar.background': colorMain,
        'activityBar.border': colorNone,
        'activityBar.foreground': colorGrey,
        'activityBarBadge.background': colorMainNegative,
        'activityBarBadge.foreground': colorMain,
        'badge.background': colorMainNegative,
        'badge.foreground': colorMain,
        'button.background': colorPrimary,
        'button.foreground': colorPrimaryNegative,
        'contrastBorder': colorNone,
        'diffEditor.insertedTextBackground': colorAddedHighlight,
        'diffEditor.removedTextBackground': colorDeletedHighlight,
        'dropdown.background': colorMainContrast,
        'dropdown.border': colorBorder,
        'dropdown.foreground': colorMainNegative,
        'editor.background': colorMain,
        'editor.findMatchBackground': colorFind,
        'editor.findMatchHighlightBackground': colorFindHighlight,
        'editor.foreground': colorMainNegative,
        'editor.lineHighlightBackground': colorPrimaryHighlightLight,
        'editor.lineHighlightBorder': colorNone,
        'editor.selectionBackground': colorPrimaryHighlightStrong,
        'editor.selectionForeground': colorMain,
        "editor.selectionHighlightBorder":
            ColorSplit(colorNone, colorPrimaryHighlight),
        'editor.wordHighlightBackground': colorPrimaryHighlight,
        'editor.wordHighlightStrongBackground': colorPrimaryHighlightStrong,
        'editorBracketMatch.background': colorPrimaryHighlightStrong,
        'editorBracketMatch.border': colorNone,
        'editorCursor.foreground': colorPrimary,
        'editorError.foreground': colorError,
        'editorGroup.border': colorMainContrast,
        'editorGroupHeader.tabsBackground': colorMain,
        'editorGroupHeader.tabsBorder': colorNone,
        'editorGutter.addedBackground': colorAdded,
        'editorGutter.deletedBackground': colorDeleted,
        'editorGutter.modifiedBackground': colorMainNegative,
        'editorIndentGuide.background': colorMainContrast,
        'editorLineNumber.foreground': ColorSplit('#ebf0f5', colorGreyLight),
        'editorLink.activeForeground': colorPrimary,
        'editorOverviewRuler.addedForeground': colorNone,
        'editorOverviewRuler.border': colorNone,
        'editorOverviewRuler.bracketMatchForeground':
            colorPrimaryHighlightStrong,
        'editorOverviewRuler.errorForeground': colorError,
        'editorOverviewRuler.findMatchForeground': colorFind,
        'editorOverviewRuler.modifiedForeground': colorMainNegative,
        'editorOverviewRuler.selectionHighlightForeground':
            colorPrimaryHighlightStrong,
        'editorOverviewRuler.warningForeground': colorWarning,
        'editorOverviewRuler.wordHighlightForeground': colorPrimaryHighlight,
        'editorOverviewRuler.wordHighlightStrongForeground':
            colorPrimaryHighlightStrong,
        'editorRuler.foreground': colorMainContrast,
        'editorSuggestWidget.foreground': colorMainNegative,
        'editorWarning.foreground': colorWarning,
        'editorWidget.background': colorMainContrast,
        'editorWidget.border': colorBorder,
        'errorForeground': colorError,
        'extensionButton.prominentBackground': colorPrimary,
        'extensionButton.prominentForeground': colorPrimaryNegative,
        'extensionButton.prominentHoverBackground': colorPrimary,
        'focusBorder': colorBorder,
        'foreground': colorMainNegative,
        'gitDecoration.ignoredResourceForeground': colorGrey,
        'gitDecoration.modifiedResourceForeground': colorMainNegative,
        'gitDecoration.untrackedResourceForeground': colorMainNegative,
        'input.background': colorMainContrast,
        'input.border': colorBorder,
        'input.foreground': colorMainNegative,
        'input.placeholderForeground': colorGrey,
        'list.activeSelectionBackground': colorMainNegative,
        'list.activeSelectionForeground': colorMain,
        'list.dropBackground': colorPrimaryHighlightStrong,
        'list.focusBackground': colorPrimaryHighlight,
        'list.focusForeground': colorMainNegative,
        'list.highlightForeground': colorMainNegative,
        'list.hoverBackground': colorMainContrast,
        'list.inactiveSelectionBackground': colorMainContrast,
        'list.inactiveSelectionForeground': colorMainNegative,
        'panel.background': colorMainContrast,
        'panel.border': colorNone,
        'panelTitle.activeBorder': colorGrey,
        'peekView.border': colorMainNegative,
        'peekViewEditor.background': colorNone,
        'peekViewEditor.matchHighlightBackground': colorFind,
        'peekViewResult.background': colorNone,
        'peekViewResult.fileForeground': colorGreyStrong,
        'peekViewResult.lineForeground': colorGreyStrong,
        'peekViewResult.matchHighlightBackground': colorFind,
        'peekViewResult.selectionBackground': colorMainNegative,
        'peekViewResult.selectionForeground': colorMain,
        'peekViewTitle.background': colorNone,
        'peekViewTitleDescription.foreground': colorGrey,
        'peekViewTitleLabel.foreground': colorMainNegative,
        'progressBar.background': colorPrimary,
        'scrollbar.shadow': colorNone,
        'scrollbarSlider.background': colorMainContrastTransparent,
        'scrollbarSlider.hoverBackground': colorMainNegative,
        'sideBar.background': colorMain,
        'sideBar.foreground': colorGreyStrong,
        'sideBarSectionHeader.background': colorMainContrast,
        'sideBarSectionHeader.foreground': colorGreyStrong,
        'sideBarTitle.foreground': colorGrey,
        'statusBar.background': colorBlack,
        'statusBar.foreground': colorGreyOnBlack,
        'statusBar.noFolderBackground': colorBlack,
        'tab.activeBackground': colorMainNegative,
        'tab.activeForeground': colorMain,
        'tab.border': colorNone,
        'tab.inactiveBackground': colorNone,
        'tab.inactiveForeground': colorGrey,
        'terminal.ansiBlack': colorMainNegative,
        'terminal.ansiBlue': colorBlue,
        'terminal.ansiBrightBlack': colorMainNegative,
        'terminal.ansiBrightBlue': colorBlue,
        'terminal.ansiBrightCyan': colorCyan,
        'terminal.ansiBrightGreen': colorGreen,
        'terminal.ansiBrightMagenta': colorPurple,
        'terminal.ansiBrightRed': colorRed,
        'terminal.ansiBrightWhite': colorWhite,
        'terminal.ansiBrightYellow': colorYellow,
        'terminal.ansiCyan': colorCyan,
        'terminal.ansiGreen': colorGreen,
        'terminal.ansiMagenta': colorPurple,
        'terminal.ansiRed': colorRed,
        'terminal.ansiWhite': colorWhite,
        'terminal.ansiYellow': colorYellow,
        'terminal.foreground': colorMainNegative,
        'terminal.selectionBackground': colorPrimaryHighlightStrong,
        'terminalCursor.foreground': colorPrimary,
        'textLink.activeForeground': colorPrimary,
        'textLink.foreground': colorPrimary,
        'titleBar.activeBackground': colorMain,
        'titleBar.activeForeground': colorGreyStrong,
        'titleBar.inactiveBackground': colorMain,
        'titleBar.inactiveForeground': colorGrey,
        'welcomePage.buttonBackground': colorMainContrast,
        'welcomePage.buttonHoverBackground': colorPrimaryHighlight,
        'widget.shadow': colorNone,
    },
    'tokenColors': [
        {
            'scope': [
                'comment',
                'string.quoted.docstring'
            ],
            'settings': {
                'foreground': colorGrey,
            },
        },
        {
            'scope': [
                'string'
            ],
            'settings': {
                'foreground': colorGreyStrong,
            },
        },
        {
            'scope': [
                'punctuation.definition.string',
                'storage.type.string.python',
            ],
            'settings': {
                'foreground': colorMainNegative,
            },
        },
        {
            'scope': [
                'beginning.punctuation',
                'entity.name.section.group-title',
                'entity.name.tag',
                'entity.other.attribute-name.class',
                'entity.other.attribute-name.id',
                'keyword.const',
                'keyword.control',
                'keyword.function',
                'keyword.import',
                'keyword.operator.assignment',
                'keyword.operator.comparison',
                'keyword.operator.decrement',
                'keyword.operator.expression',
                'keyword.operator.increment',
                'keyword.operator.increment-decrement',
                'keyword.operator.logical',
                'keyword.operator.new',
                'keyword.operator.other',
                'keyword.other.special-method',
                'keyword.package',
                'keyword.type',
                'keyword.var',
                'markup.heading',
                'meta.tag.sgml.doctype.html',
                'punctuation.separator.key-value',
                'storage.modifier',
                'storage.type.class',
                'storage.type.enum',
                'storage.type.function',
                'storage.type.import',
                'storage.type.interface',
                'storage.type.js',
                'storage.type.namespace',
                'storage.type.property',
                'storage.type.string.python',
                'storage.type.ts',
            ],
            'settings': {
                'fontStyle': 'bold',
            },
        },
    ],
}
