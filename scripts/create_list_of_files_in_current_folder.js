const { readdirSync, statSync } = require('fs');
const { join, dirname } = require('path');

// module.exports = async () => {
//     console.log(this.app.workspace);
//     // Получаем активный файл через API Obsidian
//     const activeFile = this.app.workspace.getActiveFile();
//     // console.log('file', activeFile);
//     if (!activeFile) {
//         return "No active file found.";
//     }


//     const currentFilePath = activeFile.path;
//     // Путь,  вкотором будем искать файлы
//     const currentDir = dirname(currentFilePath);
//     console.log(currentDir);

//     const files = readdirSync(currentDir).filter(file => {
//         console.log(file);
//         return statSync(join(currentDir, file)).isFile() && file.endsWith('.md');
//     });

//     console.log('files', files);
//     const fileLinks = files.map(file => `- [[${file.replace('.md', '')}]]`).join('\n');
//     console.log('fileLinks', fileLinks);
//     return fileLinks;
// };

// const activeFile = this.app.workspace.getActiveFile();
// if (activeFile) {
//     console.log("Active file path:", activeFile.path);
//     console.log("Active file name:", activeFile.basename);
// }
// module.exports = async () => {
//     const workspace = this.app.workspace;
//     // Получаем объект с информацией о всех заметках
//     const fileMap = workspace.app.vault.fileMap;
//     console.log(typeof(fileMap));
//     console.log(fileMap);

//     let noteInfo = "## Информация о заметках\n\n";

//     // Цикл по всем элементам fileMap
//     for (const filePath in fileMap) {
//         if (fileMap.hasOwnProperty(filePath)) {
//             const file = fileMap[filePath];
//             const fileName = file.name;
//             console.log(fileName);
//             // const fileCreated = file.stat.ctime.toLocaleString(); // Пример получения даты создания файла

//             // Формирование строки с информацией о файле
//             const fileInfo = `- **Имя файла:** ${fileName}\n  **Путь:** ${filePath}\n `;

//             // Добавление информации о файле в переменную noteInfo
//             noteInfo += fileInfo;
//         }
//     }

//     return noteInfo;
// };

module.exports = async () => {
    const workspace = this.app.workspace;
    const fileMap = workspace.app.vault.fileMap;

    let noteInfo = "## Ссылки на заметки в формате Markdown (.md)\n\n";

    for (const filePath in fileMap) {
        if (fileMap.hasOwnProperty(filePath)) {
            const file = fileMap[filePath];
            const fileName = file.name;

            // Проверяем, что файл имеет расширение .md
            if (fileName.endsWith('.md')) {
                // Формируем ссылку на файл
                const fileLink = `- [${fileName}](${filePath})\n`;
                noteInfo += fileLink;
            }
        }
    }

    return noteInfo;
};



