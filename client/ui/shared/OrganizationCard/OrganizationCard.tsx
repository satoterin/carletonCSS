import React from 'react';

interface Props {
  title: String;
  imgUrl: String;
}

const OrganizationCard = ({ title, imgUrl }: Props) => {
  return (
    <div className="organization-card">
      <div
        className="organization-card-image"
        style={{ backgroundImage: 'url("' + imgUrl + '")' }}
      />
      <div className="organization-card-content">
        <div className="organization-card-content-title">{title}</div>
        <button className="organization-card-button">Learn More</button>
      </div>
    </div>
  );
};

export { OrganizationCard };
