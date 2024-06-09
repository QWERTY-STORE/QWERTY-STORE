document.addEventListener("DOMContentLoaded", () => {
    const categoryButton = document.querySelector('.category-button');
    categoryButton.addEventListener('click', () => {
        alert('Категории нажаты');
    });

    const productButtons = document.querySelectorAll('.product button');
    productButtons.forEach(button => {
        button.addEventListener('click', (e) => {
            const productName = e.target.closest('.product').querySelector('h3').textContent;
            alert(`Товар ${productName} добавлен в корзину`);
        });
    });
});
