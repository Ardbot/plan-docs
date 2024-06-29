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

// module.exports = async () => {
//     const workspace = this.app.workspace;
//     const fileMap = workspace.app.vault.fileMap;

//     let noteInfo = "## Ссылки на заметки в формате Markdown (.md)\n\n";

//     for (const filePath in fileMap) {
//         if (fileMap.hasOwnProperty(filePath)) {
//             const file = fileMap[filePath];
//             const fileName = file.name;

//             // Проверяем, что файл имеет расширение .md
//             if (fileName.endsWith('.md')) {
//                 // Формируем ссылку на файл
//                 const fileLink = `- [${fileName}](${filePath})\n`;
//                 noteInfo += fileLink;
//             }
//         }
//     }

//     return noteInfo;
// };

module.exports = async () => {
    // const workspace = this.app.workspace;
    const { workspace, vault } = this.app;
    const fileMap = workspace.app.vault.fileMap;
    let noteInfo = "## Ссылки на заметки\n\n";

    console.log(fileMap);
    for (const filePath in fileMap) {
        if (fileMap.hasOwnProperty(filePath)) {
            const folder = fileMap[filePath];
            const folderName = folder.name;
            // Если папка
            if (folder?.children) {

                noteInfo += `${folderName}:\n `

                // папка с файлами
                children = folder?.children
                for (md in children) {
                    if (children.hasOwnProperty(md)) {

                        const file = children[md];
                        const fileName = file.name;
                        if (fileName.endsWith('.md')) {
                            // console.log(fileName)
                            const fileLink = `- [${fileName}](${filePath})\n`;
                            noteInfo += fileLink;
                        }
                    }
                }
                // Дополнительный отсуп
                noteInfo += `\n `

                // if (fileName) {
                //     try {
                //         const fileContent = '# Новая заметка\n\nЭто содержимое новой заметки.';
                //         // Создание нового файла в корне хранилища
                //         await vault.create(fileName, fileContent);

                //         console.log(`Файл успешно создан: ${fileName}`);
                //         return `Файл успешно создан: ${fileName}`;
                //     } catch (error) {
                //         console.error('Ошибка при создании файла: ', fileName, error);
                //         if (error == 'File already exists.') {
                //             console.log(fileName, 'уже есть');
                //             return `${error.message} уже есть`
                //         }
                //         else{
                //             return `Ошибка при создании файла: ${error.message}`;
                //         }

                //     }
                // }

            }
        }
    }
    return noteInfo;
};

// const fs = require('fs');
// const path = require('path');

// module.exports = async () => {
//     const workspace = this.app.workspace;
//     const fileMap = workspace.app.vault.fileMap;

//     for (const filePath in fileMap) {
//         if (fileMap.hasOwnProperty(filePath)) {
//             const file = fileMap[filePath];


//             // Проверяем, если текущий элемент является папкой и имеет дочерние элементы
//             if (file?.children) {
//                 const fileName = file.name;
//                 console.log(`Processing folder: ${fileName}`);
//                 // Создаем файл для записи ссылок
//                 // const outputFileName = `${folderName}_links.md`;
//                 // const outputPath = path.join(__dirname, outputFileName);
//                 // let noteInfo = `## Ссылки из папки "${folderName}"\n\n`;

//                 // Рекурсивно обходим дочерние элементы
//                 // await processChildren(file.children, noteInfo);

//                 // Записываем результат в файл
//                 // fs.writeFileSync(outputPath, noteInfo);
//                 const { vault } = this.app;
//                 try {
//                     // Имя нового файла и его содержимое
//                     const newFileName = 'Новый файл.md';
//                     const fileContent = '# Новая заметка\n\nЭто содержимое новой заметки.';

//                     console.log(fileName);
//                     // Создание нового файла в корне хранилища
//                     const newFilePath = await vault.create(newFileName, fileContent);

//                     console.log(`Файл успешно создан: ${newFilePath}`);
//                     return `Файл успешно создан: ${newFilePath}`;
//                 } catch (error) {
//                     console.error('Ошибка при создании файла: ', error);
//                     return `Ошибка при создании файла: ${error.message}`;
//                 }

//                 // console.log(`Links saved to ${outputFileName}`);
//             }
//         }
//     }
// };