import * as fs from "fs-extra";
import * as _ from "lodash";
import * as path from "path";
import { Color } from "./color";
import definitions from "./definitions";

function forgeColors(obj: any, night: boolean) {
    for (const prop in obj) {
        if (obj[prop] instanceof Color) {
            obj[prop] = night ? obj[prop].nightHex : obj[prop].hex;
        } else if (obj[prop] instanceof Object) {
            forgeColors(obj[prop], night);
        }
    }
    return obj;
}

function generate(night: boolean) {
    let filename = path.resolve(__dirname, "../themes/White");
    if (night) {
        filename += "-Night";
    }
    filename += "-color-theme.json";

    fs.outputJson(filename, forgeColors(_.cloneDeep(definitions), night), {
        spaces: 4,
    });
}

generate(false);
generate(true);
