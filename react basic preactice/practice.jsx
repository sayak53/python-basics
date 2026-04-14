const Name = () => {
  const name = "Sayak";

  return (
    <div>
      <h1>Hello {name}</h1>
    </div>
  );
};

const Location = () => {
  const city = "Kolkata";

  return (
    <div>
      <h1>I Live in {city}</h1>
    </div>
  );
};

const MathTask = () => {
  return <h1>15 + 12 = {15 + 12}</h1>;
};
