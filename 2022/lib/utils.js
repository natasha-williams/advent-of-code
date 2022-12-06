

const formatData = ({ data, splitAt='\n', parseFn=null }) => {
    return data.split(splitAt).map(item => {
        return parseFn ? parseFn(item) : item;
    });
};


const getChunks = (data, num) => {
    return [...Array(Math.ceil(data.length / num))].map(() => data.splice(0, num));
};


const getTotal = (data) => {
    return data.reduce((sum, next) => sum + next, 0);
};


export {
    formatData,
    getChunks,
    getTotal,
};
