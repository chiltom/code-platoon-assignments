import PropTypes from "prop-types";
import axios from "axios";
import Button from "react-bootstrap/Button";

const PageButtons = ({ nextPage, prevPage, setCharacters }) => {
  const handleNext = async () => {
    const { data } = await axios.get(nextPage);
    setCharacters(data);
  };

  const handlePrev = async () => {
    const { data } = await axios.get(prevPage);
    setCharacters(data);
  };

  return (
    <>
      <div className="flex flex-row justify-evenly">
        {prevPage ? (
          <Button
            size="sm"
            variant="secondary"
            className="w-60 bg-slate-500"
            onClick={(e) => {
              e.preventDefault();
              handlePrev();
            }}
          >
            Previous Page
          </Button>
        ) : null}
        {nextPage ? (
          <Button
            size="sm"
            variant="secondary"
            className="w-60 bg-slate-500"
            onClick={(e) => {
              e.preventDefault();
              handleNext();
            }}
          >
            Next Page
          </Button>
        ) : null}
      </div>
    </>
  );
};

PageButtons.propTypes = {
  nextPage: PropTypes.string,
  prevPage: PropTypes.string,
  setCharacters: PropTypes.func,
};

export default PageButtons;
