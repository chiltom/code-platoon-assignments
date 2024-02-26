// Function to replace images with their alt text
const replaceImages = () => {
    const imgs = Array.from(document.getElementsByTagName('img'));
    imgs.map((img) => {
        if (img.alt) {
            const txt = document.createTextNode(img.alt);
            img.parentNode.replaceChild(txt, img);
        }
    })
};