module.exports = async () => {
    const { vault } = this.app;

    try {
        // Имя нового файла и его содержимое
        const newFileName = 'Новый файл.md';
        const fileContent = '# Новая заметка\n\nЭто содержимое новой заметки.';

        // Создание нового файла в корне хранилища
        const newFilePath = await vault.create(newFileName, fileContent);

        console.log(`Файл успешно создан: ${newFilePath}`);
        return `Файл успешно создан: ${newFilePath}`;
    } catch (error) {
        console.error('Ошибка при создании файла:', error);
        return `Ошибка при создании файла: ${error.message}`;
    }
};