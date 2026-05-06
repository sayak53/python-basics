const Name = () => {
  const name = "Sayak";

  return (
    <div>
      <h1>Hello {name}</h1>
    </div>
  );
};

const Location = () => {
  const city = "Mumbai";

  return (
    <div>
      <h1>I Live in {city}</h1>
    </div>
  );
};

const Addition = () => {
  return <h1>10 + 5 = {10 + 5}</h1>;
};

const Substraction = () => {
  return <h1>100 - 5 = {100 - 5}</h1>;
};

const Multiply = () => {
  return <h1>10 * 5 = {10 * 5}</h1>;
};

import React from "react";

export const practice = () => {
  return <div>practice</div>;
};
